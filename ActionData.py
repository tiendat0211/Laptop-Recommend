from pandas import read_csv
from Laptop import Laptop
NORECORD = 'chưa có thông tin'

class ActionData:
    # mảng chứa các thuộc tính của game
    properties = []
    # mục đang hiển thị
    selection = 0
    # Sự kiện kết thúc tải giao diện người dùng giao diện chính được liên kết với thuộc tính WHEN CHANGED của load_properties ()
    # Tải tệp csv trong thư mục được chỉ định để tạo tất cả các phiên bản
    def load_properties(self, csv_filepath):
        # WHEN CHANGED
        dataFrame = read_csv(csv_filepath)
        # dữ liệu NaN được xử lý ở đây (Thay thế data null bằng NORECORD)
        dataFrame.fillna(NORECORD, inplace = True)
        # _ là index, iterrows là mảng dữ liệu (thư viện pandas)
        for _, row in dataFrame.iterrows():
            # nạp dữ liệu file csv vào đối tượng VideoGame và lưu vào private games[]
            Laptop(row)
        # lưu dữ liệu games của VideoGame vào game_list
        game_list = Laptop.laptops
        return game_list
    
    # Thay đổi nội dung của các trò chơi được đề xuất ở định dạng được chỉ định
    def change_display(self):
        properties = ActionData.properties
        selection = ActionData.selection
        display_message = '\nTìm thấy cho bạn {} Laptop, hiện đang hiển thị {} mục\nHãng :{}\nTên :{}\nLoại :{}\nMàn hình:{}\nKích thước màn hình:{}\nCPU:{}\nRAM:{}\nBộ nhớ:{}\nGPU:{}\nHệ điều hành:{}\nPhiên bản hệ điều hành:{}\nCân nặng:{}\nGiá($):{}\n'.format(
                                len(properties), selection+1,
                                properties[selection].brand, properties[selection].model,properties[selection].category, properties[selection].screen,
                                properties[selection].screen_size, properties[selection].cpu,properties[selection].ram, properties[selection].storage,
                                properties[selection].gpu, properties[selection].operating_system, properties[selection].operating_system_version, properties[selection].weight,properties[selection].price)
        return display_message

    def goto_next_property(self):
        # WHEN CHANGED
        if ActionData.selection < len(ActionData.properties) - 1:
            ActionData.selection += 1
        return self.change_display()

    def goto_prev_property(self):
        # WHEN CHANGED
        if ActionData.selection > 0:
            ActionData.selection -= 1
        return self.change_display()