NORECORD = 'chưa có thông tin'

class Laptop:
    laptops = []
    # set tương tự oject, tạo 1 đối tượng
    Brand = set()
    Model = set()
    Category = set()
    Screen_Size = set()
    Screen=set()
    RAM = set()
    CPU = set()
    Storage = set()
    GPU=set()
    Operating_System =set()
    Operating_System_Version =set()
    Weight=set()
    Price = set ()
    
    # hàm khởi tạo đối tương trong python (__init__)
    def __init__(self, data):
        # Khởi tạo đối tượng
        # Dữ liệu bị thiếu được thay thế bằng chuỗi no_record
        self.brand = data.Brand
        self.model = data.Model
        self.category = data.Category
        self.screen_size = data.Screen_Size
        self.screen = data.Screen
        self.cpu = data.CPU
        self.ram = data.RAM
        self.storage = data.Storage
        self.gpu = data.GPU
        self.operating_system = data.Operating_System
        self.operating_system_version = data.Operating_System_Version
        self.weight = data.Weight

        try:
            self.price = round(float(data.Price), 2)
        except ValueError:
            self.price = NORECORD

        # ghi loại trò chơi
        Laptop.Brand.add(self.brand)

        # Tránh các loại trò chơi NaN trong menu thả xuống
        if self.category != NORECORD:
            Laptop.Category.add(self.category)

        if self.ram != NORECORD:
            Laptop.RAM.add(self.ram)

        if self.cpu != NORECORD:
            Laptop.CPU.add(self.cpu)

          # Tránh các loại trò chơi NaN trong menu thả xuống
        if self.storage != NORECORD:
            Laptop.Storage.add(self.storage)


        Laptop.laptops.append(self)

    # In ra các loại trò chơi của các tệp dữ liệu được thu thập thông tin
    @ classmethod
    def show_brand(cls):
        print(len(cls.Brand), ' Brand in total: ')
        
    # Có những nền tảng trò chơi nào để in ra các tệp dữ liệu đã thu thập thông tin?
    @ classmethod
    def show_category(cls):
        print(len(cls.Category), ' Category in total: ')
    
     # Có những nền tảng trò chơi nào để in ra các tệp dữ liệu đã thu thập thông tin?
    @ classmethod
    def show_cpu(cls):
        print(len(cls.CPU), ' CPU in total: ')

     # Có những nền tảng trò chơi nào để in ra các tệp dữ liệu đã thu thập thông tin?
    @ classmethod
    def show_ram(cls):
        print(len(cls.RAM), ' RAM in total: ')

    @ classmethod
    def show_storage(cls):
        print(len(cls.Storage), ' Storage in total: ')
