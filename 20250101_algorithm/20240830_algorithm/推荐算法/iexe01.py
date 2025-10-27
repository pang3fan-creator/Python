import numpy as np
import pandas as pd

data = pd.read_json('../data_test/ratings.json')
data_corr = data.corr()['Michael Henry']
data_corr = data_corr[data_corr > 0.6][data_corr != 1]

# {'电影A':[[打分1,打分2,...],[相似度1,相似度2,...]],...}
data_movie = {}
for k, v in data_corr.items():
    for i, j in data[k].dropna().items():
        if i not in data['Michael Henry'].dropna().keys():
            data_movie.setdefault(i, [[], []])
            data_movie[i][0].append(j)
            data_movie[i][1].append(v)

score_movie = [(k, np.dot(v[0], v[1])) for k, v in data_movie.items()]
score_movie = sorted(score_movie, key=lambda x: x[1], reverse=True)
print(score_movie)
