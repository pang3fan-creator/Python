"""
一张纸0.01毫米 20次对折后多少毫米？
"""
thickness = 0.01
for count in range(20):
    thickness *= 2

print(f"厚度是：{thickness}毫米")
