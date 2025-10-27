def get_score():
    while True:
        try:
            score = int(input("请输入分数："))
            if score < 0 or score > 100:
                continue
            else:
                return score
        except:
            print("输入错误，请重新输入")


score = get_score()
print(f"分数是：{score}")
