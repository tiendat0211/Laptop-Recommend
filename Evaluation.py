NORECORD = 'chưa có thông tin'

class Evaluation():
    def __init__(self, args):
        self.brand = args['brand']
        self.cpu = args['cpu']
        self.category = args['category']
        self.ram = args['ram']
        self.storage = args['storage']

    # các lựa chọn của người dùng
    def print_rule(self):
        print('【RULE】',self.brand, self.cpu, self.category, self.ram, self.storage)

    # sử dụng luật đưa ra kết quả
    def qualified(self, laptop):
        print(laptop.brand)
        return laptop.brand == self.brand and laptop.category == self.category