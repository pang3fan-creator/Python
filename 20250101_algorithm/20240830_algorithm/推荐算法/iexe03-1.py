import numpy as np
import pandas as pd


class ItemCF(object):
    def __init__(self):
        # '../data_test/movielens电影数据/ratings.dat',取前一千条!
        self.__data = pd.read_csv('./movie.csv', sep=',', header=None, engine='python')
        self.data_movie = self.num_movies = self.mat_movie = self.sim_movie = self.rec_movie = {}

    def main(self, user, a, b):
        self.datamovie()
        self.matmovie()
        self.simmovie()
        self.recmovie(user, a, b)

    def datamovie(self):
        # {user:{电影1:打分,电影2:打分,....},.....}
        for i in range(self.__data.shape[0]):
            self.data_movie.setdefault(self.__data.iloc[i, 0], {})
            self.data_movie[self.__data.iloc[i, 0]][self.__data.iloc[i, 1]] = self.__data.iloc[i, 2]

    def matmovie(self):
        # 记录每个电影被看了了多少次  {'电影1':次数,'.....}
        num_movies = {}
        for user, movies in self.data_movie.items():
            for movie, score in movies.items():
                num_movies.setdefault(movie, 0)
                num_movies[movie] += 1

        # 电影和电影的共现矩阵 {电影1:{电影2:次数,电影3:次数,...},....}
        matrix_movie = {}
        for k in num_movies.keys():
            matrix_movie.setdefault(k, {})
            for j in self.data_movie.values():
                for x in j.keys():
                    if x != k and k in j.keys():
                        matrix_movie[k].setdefault(x, 0)
                        matrix_movie[k][x] += 1

    def simmovie(self):
        for k, v in self.mat_movie.items():
            self.sim_movie.setdefault(k, {})
            for i, j in v.items():
                self.sim_movie[k][i] = j / (self.num_movies[i] * self.num_movies[k]) ** 0.5

    def recmovie(self, user, a, b):
        # {推荐电影:推荐值}
        for k, v in self.data_movie[user].items():
            temp_movie = sorted(self.sim_movie[k].items(), key=lambda x: x[1], reverse=True)[:a:]
            for i, j in temp_movie:
                if i not in self.data_movie[user].keys():
                    self.rec_movie.setdefault(i, 0)
                    self.rec_movie[i] += j * v
        self.rec_movie = sorted(self.rec_movie.items(), key=lambda x: x[1], reverse=True)[:b:]


if __name__ == '__main__':
    icf = ItemCF()
    icf.main(user=3, a=10, b=10)
    print(icf.rec_movie)
