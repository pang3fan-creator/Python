"""
创建3个列表
地区  台湾 北京 天津
新增人数： 300 861 465
现有人数： 2654 8456，4566

在陕西 新发现 60人感染 需要把地区和人数分别添加到各个列表中
香港发现45人感染， 把香港的相关信息排在台湾后边
今日新增人数最多的地区人数
累计人数最少的地区人数
"""
list_region = ["台湾", "北京", "天津"]
list_new = [300, 864, 465]
list_now = [2654, 8456, 4566]

list_region.append("陕西")
list_new.append(60)
list_now.append(60)

list_region.insert(1, "香港")
list_new.insert(1, 45)
list_now.insert(1, 45)
print(list_region, list_new, list_now)
print(max(list_new))
print(min(list_now))
