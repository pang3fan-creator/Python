"""
    练习：画出下列代码内存图1
"""
list_region = ["台湾", "陕西", "浙江"]
data01 = list_region
data02 = list_region[-2:]
data02[0] = "shan_xi"
print(list_region)
data01[0] = "tai_wan"
print(list_region)
