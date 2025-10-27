import numpy as np
import pandas as pd

if __name__ == '__main__':
    # '../data_test/movielens电影数据/ratings.dat',取前一千条!
    data = pd.read_csv('./movie.csv', sep=',', header=None, engine='python')

    # {user:{电影1:打分,电影2:打分,....},.....}
    data_movie = {}
    for i in range(data.shape[0]):
        data_movie.setdefault(data.iloc[i, 0], {})
        data_movie[data.iloc[i, 0]][data.iloc[i, 1]] = data.iloc[i, 2]

    # 记录每个电影被看了了多少次  {'电影1':次数,'.....}
    num_movies = {}
    for user, movies in data_movie.items():
        for movie, score in movies.items():
            num_movies.setdefault(movie, 0)
            num_movies[movie] += 1

    # 电影和电影的共现矩阵 {电影1:{电影2:次数,电影3:次数,...},....}
    matrix_movie = {}
    for k in num_movies.keys():
        matrix_movie.setdefault(k, {})
        for j in data_movie.values():
            for x in j.keys():
                if x != k and k in j.keys():
                    matrix_movie[k].setdefault(x, 0)
                    matrix_movie[k][x] += 1
    similarity_movie = {}

    # {电影1:{电影2:相似度,...},....}
    for k, v in matrix_movie.items():
        similarity_movie.setdefault(k, {})
        for i, j in v.items():
            similarity_movie[k][i] = j / (num_movies[i] * num_movies[k]) ** 0.5

    # {推荐电影:推荐值}
    user = 3
    recommend_movie = {}
    for k, v in data_movie[user].items():
        temp_movie = sorted(similarity_movie[k].items(), key=lambda x: x[1], reverse=True)[:10:]
        for i, j in temp_movie:
            if i not in data_movie[user].keys():
                recommend_movie.setdefault(i, 0)
                recommend_movie[i] += j * v
    recommend_movie = sorted(recommend_movie.items(), key=lambda x: x[1], reverse=True)[:20:]
    print(recommend_movie)
