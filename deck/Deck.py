# 初始化一副扑克牌
# 熟悉列表推导的使用
# list 的操作符重载
# namedtuple 数据结构
# 魔法方法
# python 的数据模型
from collections import namedtuple

class Deck:
    '''
    一副扑克牌
    '''
    Ranks = [str(i) for i in range(2, 11)] + list("JQKA")
    Suites = ["Diamond", "Club", "Heart", "Spade"]
    Card = namedtuple("Card", ["rank", "suite"])

    def __init__(self):
        self.cards = [ self.Card(rank=rank, suite=suite) for rank in self.Ranks
                       for suite in self.Suites]

    def __len__(self):
        '''
        获取数量
        :return: 一副扑克牌的数量 
        '''
        return len(self.cards)

    def __repr__(self):
        pass

    def __getitem__(self, item):
        '''
        获取 一副扑克牌某个位置的牌是什么
        :param item: 位置索引 
        :return:  单张扑克牌 
        '''
        return self.cards[item]

if __name__ == "__main__":
    d = Deck()
    for card in d:
        print(card)

