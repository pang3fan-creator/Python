import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

ret = []
with open('../20240830_tuijiansuanfa/Apriori_data.txt', 'r') as f:
    for line in f.readlines():
        ret.append(line.strip().split(','))

te = TransactionEncoder()
te_ary = te.fit(ret).transform(ret)

pd_ary = pd.DataFrame(te_ary, columns=te.columns_)
fp_items = fpgrowth(pd_ary, min_support=0.4, use_colnames=True)

print(fp_items)
rules = association_rules(fp_items, min_threshold=0.4)
print(type(rules))
# print(rules)
