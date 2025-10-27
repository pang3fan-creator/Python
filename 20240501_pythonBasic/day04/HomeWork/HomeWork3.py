"""
一个小球从100m高度落下,每次弹回原高度一半.
       计算:
        -- 总共弹起多少次?(最小弹起高度0.01m)
        -- 全过程总共移动多少米?
    数据： 高度       次数       距离
    处理： 高度/=2    次数+=1    距离+=？
"""
height = 100
count = 0
# 计算移动多少米
distance = height
while height / 2 > 0.01:
    height /= 2
    distance += height * 2
    count += 1
    print(f"第{count}次弹起来的高度是{height}")

print(f"共弹起{count}次")  # 13
print(f"共移动{distance}米")  # 299.97
