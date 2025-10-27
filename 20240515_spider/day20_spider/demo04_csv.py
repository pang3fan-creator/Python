"""
    demo04_csv.py
"""
import csv

# 单行写入
with open("test.csv", "w", encoding="utf-8", newline="") as f:
    # 创建csv文件的写入对象
    writer = csv.writer(f)
    # 写入数据
    writer.writerow([1, "聂风", "雪饮狂刀"])


# 多行写入
with open("test.csv", "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows([[2,"步惊云","绝世好剑"],[3,"断浪","火麟剑"]])


# 单行写入
f = open("test.csv", "a", encoding="utf-8", newline="")
writer = csv.writer(f)
writer.writerow([4,"雄霸","三分归元气"])
f.close()

















