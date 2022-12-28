NORECORD = 'chưa có thông tin'

class Evaluation():
    def __init__(self, args):
        self.platform = args['pf']
        self.genre = args['ge']
        self.lb = args['lb']
        self.rb = args['rb']
        self.critic_score = args['cs']
        self.user_score = args['us']
        self.allowed_rating = args['ar']

    # các lựa chọn của người dùng
    def print_rule(self):
        print('【RULE】',self.platform, self.genre, self.lb, self.rb, self.critic_score, self.user_score)

    # sử dụng luật đưa ra kết quả
    def qualified(self, game):
        return game.platform == self.platform and game.genre == self.genre \
            and (game.year_of_release == NORECORD or game.year_of_release >= self.lb and game.year_of_release <= self.rb)\
                and (game.critic_score == NORECORD or game.critic_score >= self.critic_score) \
                    and(game.user_score == NORECORD or game.user_score >= self.user_score)\
                        and(game.rating == NORECORD or game.rating in self.allowed_rating)