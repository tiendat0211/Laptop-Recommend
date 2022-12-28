import os
import time
from time import sleep
from pandas import read_csv
from tkinter import Label, Frame, Button, Checkbutton, Tk, IntVar, HORIZONTAL, Scale, filedialog
from tkinter import ttk
from Laptop import Laptop
from ActionData import ActionData
from Evaluation import Evaluation

NORECORD = 'chưa có thông tin'
# Một danh sách các intVars được liên kết với chín xếp hạng khác nhau. Khi nó là 1, điều đó có nghĩa là nó đã được chọn
intVar = []
# Bản ghi thứ n hiện đang được hiển thị, có thể được chuyển đổi bằng nút
selection = 0
# Lưu tất cả các bản ghi trò chơi trong cơ sở dữ liệu
laptop_list = []

# [Gọi phương thức lớp ActionData] Thay đổi nội dung hiển thị giao diện người dùng theo tương tác của người dùng
# Phương thức WHEN CHANGED kích hoạt goto_prev_property và goto_next_property
def switch_property(direction):
    if direction == 'prev':
        message = action_data_agent.goto_prev_property()
    else:
        message = action_data_agent.goto_next_property()
    result_message['text'] = message


# [Daemon] Duyệt qua hàng đợi game_list để tìm các phiên bản đủ điều kiện theo điều kiện truy xuất của người dùng
# Liên kết các thành phần giao diện với daemon và xóa các phiên bản không phù hợp
# Lưu trữ các phiên bản đủ điều kiện trong ActionData.properties
def properties_filter():
    # Nhận các điều kiện truy vấn do người dùng chọn trong giao diện từ mỗi thành phần
    ActionData.properties.clear()
    
    args = {'brand': brand_select.get(),
            'cpu': cpu_select.get(),
            'category': category_select.get(),
            'ram': ram_select.get(),
            'storage': storage_select.get()}

    evaluate = Evaluation(args)
    evaluate.print_rule()

    for laptop in laptop_list:
        if evaluate.qualified(laptop):
            ActionData.properties.append(laptop)
    
    # Kết quả lựa chọn thiết bị đầu cuối đáp ứng yêu cầu của người dùng
    print('【RESULT】', len(ActionData.properties))
    # Sắp xếp kết quả tìm kiếm theo năm theo thứ tự ngược lại
    ActionData.properties = sorted(ActionData.properties, key=lambda laptop: laptop.price if type(laptop.price) == int else -1, reverse=True)
    # Hiển thị bản ghi đầu tiên phù hợp với yêu cầu của người dùng trong cửa sổ
    # Cho dù số lượng kết quả kiểm tra là> 0
    if len(ActionData.properties):
        ActionData.selection = 0
        result_message['text'] = action_data_agent.change_display()
    else:
        result_message['text'] = 'Không có trò chơi phù hợp nào trong cơ sở dữ liệu'


if __name__ == '__main__':

    window = Tk()
    window.title("Play-Smart.expertsystem")
    window.geometry('1050x640')
    window.iconbitmap('./logo.ico')
    window.resizable(width=False, height=False)

    # Thông tin trò chơi được đề xuất được đặt ở hàng thứ 0 và hàng đầu tiên cho người dùng
    message = Label(window, text='[EXPERT SYSTEM]', font=('Microsoft YaHei', 18))
    result_window = Frame(window, width=1024, height=180)
    # Giữ kích thước cửa sổ không thay đổi
    result_window.propagate(0)
    message.grid(row=0, columnspan=10)
    result_message = Label(result_window, text='Chưa có nội dung được đề xuất')
    result_message.pack()
    result_window.grid(row=1, columnspan=10)

    # Hàng thứ hai đặt nút, khi có nhiều thông tin được đề xuất, hãy sử dụng nút để chuyển
    prev_btn = Button(window, text='Trước', command=lambda:switch_property('prev'))
    next_btn = Button(window, text='Tiếp theo', command=lambda:switch_property('next'))
    prev_btn.grid(row=2, column=3, sticky='e', ipadx=20, pady=30)
    next_btn.grid(row=2, column=4, ipadx=20)

    # Dòng thứ ba được sử dụng để chọn nền tảng và loại trò chơi của trò chơi
    brand_label = Label(window, text='Hãng Lap top', font=('tMicrosoft YaHei',12,'bold'))
    cpu_label = Label(window, text='CPU', font=('tMicrosoft YaHei',12,'bold'))
    category_label = Label(window, text='Loại Lap top', font=('tMicrosoft YaHei',12,'bold'))
    brand_select = ttk.Combobox(window)
    cpu_select = ttk.Combobox(window)
    category_select= ttk.Combobox(window)
    brand_label.grid(row=3, column=0)
    brand_select.grid(row=3, column=1)
    category_label.grid(row=3, column=2)
    category_select.grid(row=3, column=3)
    cpu_label.grid(row=4, column=0)
    cpu_select.grid(row=4, column=1)

    # Dòng thứ tư, chọn khoảng thời gian phát hành trò chơi
    ram_label = Label(window, text='RAM', font=('tMicrosoft YaHei',12,'bold'))
    storage_label = Label(window, text='Bộ nhớ', font=('tMicrosoft YaHei',12,'bold'))
    storage_select = ttk.Combobox(window)
    ram_select = ttk.Combobox(window)
    ram_label.grid(row=4, column=2)
    ram_select.grid(row=4, column=3)
    storage_label.grid(row=4, column=4)
    storage_select.grid(row=4, column=5)

    # # Dòng thứ năm, yêu cầu điểm số trò chơi
    # critical_score_scale = Scale(window, label='Xếp hạng phương tiện truyền thông cao hơn', from_=0, to=100, orient=HORIZONTAL,
    #          length=400, showvalue=1, tickinterval=10, resolution=1)
    # critical_score_scale.grid(row=5, column=0, columnspan=2)
    # user_score_scale = Scale(window, label='Đánh giá của công chúng cao hơn', from_=0, to=10, orient=HORIZONTAL,
    #          length=400, showvalue=1, tickinterval=1, resolution=0.1)
    # user_score_scale.grid(row=5, column=2, columnspan=2)

    # Dòng thứ sáu, xác nhận để gửi các yêu cầu về chỉ số trò chơi đã chọn
    submit_btn = Button(window, text='Gửi đi', font=('Microsoft YaHei', 15), command=properties_filter)
    submit_btn.grid(row=7, column=2, ipadx=70, ipady=10, pady=10)

    # # Cột ngoài cùng bên phải đặt danh sách Nhóm để chọn xếp hạng trò chơi
    # rating_frame = Frame(window)
    # rating_frame.grid(row=3, column=4, rowspan=3)
    # rating_note_label = Label(rating_frame, text='Lựa chọn xếp hạng trò chơi', font=('tMicrosoft YaHei',12,'bold'))
    # rating_note_label.pack()
    # for idx in range(len(rating_list)):
    #     intVar.append(IntVar(value=1))
    #     check = Checkbutton(rating_frame, text=rating_list[idx], variable=intVar[idx], onvalue=1, offvalue=0)
    #     check.pack(side='top', expand='yes', fill='both')
    
    # [Tải thuộc tính] Tải tệp csv sau khi tải giao diện người dùng
    # Tạo đối tượng ActionData action_data_agent
    # Kích hoạt KHI When_change để khởi tạo tất cả các bản ghi trong cơ sở dữ liệu
    print('SYSTEM: Đang chọn tải tệp CSV')
    print('SYSTEM: Thư mục hiện tại', os.getcwd())
    try:
        result_message['text'] = 'Tải dữ liệu...'
        csv_filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title='Chọn tệp csv')
        start = time.time()
        print('SYSTEM: Tệp csv đang tải...')
        action_data_agent = ActionData()
        laptop_list = action_data_agent.load_properties(csv_filepath)
        counter = round(time.time() - start, 2)
        result_message['text'] = 'Dữ liệu được tải, mất thời gian{}s, Chưa có nội dung được đề xuất'.format(counter)
        print('SYSTEM: Tệp csv đã được tải, mất thời gian{}s'.format(counter))
    except Exception:
        print('ERROR: Không tải được tệp CSV')
        window.destroy()
        sleep(1)
        exit()

    # Tải nội dung của menu thả xuống trên trang chủ theo dữ liệu
    brand_select['value'] = sorted(list(Laptop.Brand))
    cpu_select['value'] = sorted(list(Laptop.CPU))
    category_select['value'] = sorted(list(Laptop.Category))
    ram_select['value'] = sorted(list(Laptop.RAM))
    storage_select['value'] = sorted(list(Laptop.Storage))

    # Được sử dụng cho các loại thuộc tính cụ thể và nội dung cụ thể trong các bảng đầu ra ban đầu
    Laptop.show_brand()
    Laptop.show_category()
    Laptop.show_ram()
    Laptop.show_cpu()
    Laptop.show_storage()

    window.mainloop()