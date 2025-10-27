'''
通过接口实现Apriori
!pip install apyori
'''
from apyori import apriori

# 加载数据
ret = []
with open('./Apriori_data.txt', 'r') as f:
    for line in f.readlines():
        ret.append(line.strip().split(','))

res = list(apriori(ret, min_support=0.5, min_confidence=0.7))

# 关联规则
for r in res:
    base = r.ordered_statistics[0].items_base
    add = r.ordered_statistics[0].items_add
    confidence = r.ordered_statistics[0].confidence
    lift = r.ordered_statistics[0].lift
    print(f'买了:{base},推荐:{add},置信度:{confidence},提升度:{lift}')

# print(res)

# 频繁项集
# for r in res:
#     print(r.items)
# [RelationRecord(items=frozenset({'bread'}),
#                 support=0.7,
#                 ordered_statistics=[OrderedStatistic(items_base=frozenset(),
#                                                      items_add=frozenset({'bread'}),
#                                                      confidence=0.7, lift=1.0)]),
