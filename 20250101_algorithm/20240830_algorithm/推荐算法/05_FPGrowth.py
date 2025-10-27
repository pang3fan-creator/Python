'''
通过API实现FPGrowth
! sudo pip install mlxtend -i https://pypi.tuna.tsinghua.edu.cn/simple
'''
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

# 加载数据
ret = []
with open('../20240830_tuijiansuanfa/Apriori_data.txt', 'r') as f:
    for line in f.readlines():
        ret.append(line.strip().split(','))

# 将数据通过TransactionEncoder转为FPGrowth需要的数据格式
te = TransactionEncoder()
te_ary = te.fit(ret).transform(ret)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 应用FPGrowth算法(频繁项集)
fp_items = fpgrowth(df, min_support=0.4, use_colnames=True)

# 关联规则
rules = association_rules(fp_items, min_threshold=0.7)
