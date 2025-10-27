'''
基于物品的协同过滤
'''
import math


class ItemBasedCF:

    def __init__(self, data_file):
        self.data_file = data_file
        self.read_data()

    # {user:{电影1:打分,电影2:打分,....},.....}
    def read_data(self):
        self.data = {}
        with open(self.data_file, 'r') as f:
            for line in f:
                user, item, score, time = line.strip().split(',')
                self.data.setdefault(user, {})  # {user:{}}
                self.data[user][item] = int(score)

    # 计算相似度
    def item_smilarity(self):
        N = {}  # 记录每个物品被购买了多少次  {'物品1':次数,'.....}
        C = {}  # 物品和物品的共现矩阵 {物品1:{物品2:次数,物品3:次数,...},....}

        # 遍历所有数据，获得用户触发过行为的数据
        for user, items in self.data.items():
            # user:用户    items: {电影1:打分,电影2:打分,....}
            for i in items.keys():
                N.setdefault(i, 0)
                N[i] += 1
                C.setdefault(i, {})  # {物品1:{}}
                for j in items.keys():
                    if i == j:
                        continue
                    C[i].setdefault(j, 0)
                    C[i][j] += 1

        # 计算相似度矩阵
        self.W = {}  # {物品1:{物品2:相似度,...},....}
        for i, related_items in C.items():
            # related_items  {物品2:次数,...}
            self.W.setdefault(i, {})  # {物品1:{}}
            for j, cij in related_items.items():
                self.W[i][j] = cij / math.sqrt(N[i] * N[j])

        return self.W

    # 计算推荐值，进行推荐
    def recommend(self, user, K=3, N=10):
        # 拿到user触发过行为的商品
        action_item = self.data[user]  # {电影1:打分,......}
        rec_movies = {}  # {推荐电影:推荐值}

        # 遍历行为商品，找到相似商品
        for item, score in action_item.items():
            # 拿到和行为商品最相似的前k个商品
            for j, wj in sorted(self.W[item].items(), key=lambda x: x[1], reverse=True)[:K]:
                # 判断相似商品是否被登录用户看过
                if j in action_item.keys():
                    continue
                rec_movies.setdefault(j, 0)
                rec_movies[j] += wj * score

        # 按照推荐值倒序排序,取出前N的推荐电影
        return dict(sorted(rec_movies.items(), key=lambda x: x[1], reverse=True)[:N])


if __name__ == '__main__':
    icf = ItemBasedCF('item.csv')
    icf.item_smilarity()
    res = icf.recommend('3')
    # print(res)
