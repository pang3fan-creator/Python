from apyori import apriori

ret = []
with open('./Apriori_data.txt', 'r') as f:
    for line in f.readlines():
        ret.append(line.strip().split(','))
# res=list()

res = list(apriori(ret, min_support=0.5, min_confidence=0.7))
for r in res:
    base = r.ordered_statistics[0].items_base
    add = r.ordered_statistics[0].items_add
    confidence = r.ordered_statistics[0].confidence
    print(base, add, confidence)
