NORECORD = 'chưa có thông tin'

class VideoGame:
    games = []
    # set tương tự oject, tạo 1 đối tượng
    # Nền tảng
    Platform = set()
    # thể loại
    Genre = set()
    # Năm phát hành
    YearOfRelease = set()
    
    # hàm khởi tạo đối tương trong python (__init__)
    def __init__(self, data):
        # Khởi tạo đối tượng
        # Dữ liệu bị thiếu được thay thế bằng chuỗi no_record
        self.name = data.id
        self.platform = data.brand
        self.model = data.model
        try:
            self.year_of_release = int(data.ram) 
        except ValueError:
            self.year_of_release = NORECORD
        
        self.genre = data.hd_type
        self.publisher = data.graphic_card_brand
        self.global_sales = data.os

        try:
            self.critic_score = int(data.hd_size)
        except ValueError:
            self.critic_score = NORECORD
        try:
            self.user_score = round(float(data.screen_size), 1)
        except ValueError:
            self.user_score = NORECORD
        self.developer = data.processor_brand
        self.rating = data.processor_model
        # ghi loại trò chơi
        VideoGame.Platform.add(self.platform)
        # Tránh các loại trò chơi NaN trong menu thả xuống
        if self.genre != NORECORD:
            VideoGame.Genre.add(self.genre)
        if self.year_of_release != NORECORD:
            VideoGame.YearOfRelease.add(int(self.year_of_release))
        VideoGame.games.append(self)

    # In ra các loại trò chơi của các tệp dữ liệu được thu thập thông tin
    @ classmethod
    def show_genre(cls):
        print(len(cls.Genre), ' genres in total: ', cls.Genre)
        
    # Có những nền tảng trò chơi nào để in ra các tệp dữ liệu đã thu thập thông tin?
    @ classmethod
    def show_platform(cls):
        print(len(cls.Platform), ' platforms in total: ', cls.Platform)
