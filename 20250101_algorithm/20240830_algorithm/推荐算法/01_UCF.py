'''
基于用户的协同过滤
'''
import pandas as pd
import numpy as np

data = pd.read_json('../data_test/ratings.json')

# 登录用户
login_user = 'Michael Henry'
# 皮尔逊相关系数
sim_mat = data.corr()

sim_scores = sim_mat[login_user]
# 拿到所有强相关的用户
sim_scores = sim_scores[sim_scores > 0.6]
# 删除自己与自己的相关系数
sim_scores = sim_scores.drop(login_user)

# {'电影A':[[打分1,打分2,...],[相似度1,相似度2,...]],...}
rec_movies = {}

# 遍历sim_scores,拿到每一个相似用户都看过哪些电影
for sim_user, sim_score in sim_scores.items():
    # 拿到每一个相似用户都看过哪些电影
    sim_movies = data[sim_user].dropna()

    for m, s in sim_movies.items():
        # 判断登录用户是否看过m这部电影

        if np.isnan(data[login_user][m]):
            # 登录用户没看过这部电影，记录
            if m not in rec_movies.keys():
                rec_movies[m] = [[], []]
            rec_movies[m][0].append(s)
            rec_movies[m][1].append(sim_score)

# 计算推荐值(打分*相似度，整体求和)，并进行倒序排序
for m, val in sorted(rec_movies.items(), key=lambda x: np.dot(x[1][0], x[1][1]), reverse=True):
    rec_val = np.dot(val[0], val[1])
print(rec_movies)
