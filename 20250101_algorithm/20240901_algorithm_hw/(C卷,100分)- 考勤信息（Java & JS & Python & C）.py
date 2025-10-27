def isAward(record):
    absent, present = 0, 0
    late_leaveearly = ("late", "leaveearly")

    preRecord = ""  # 前一次的考勤记录

    for i in range(len(record)):
        # 滑窗长度最大为7，如果超过7，则滑窗的左边界需要右移, 滑窗失去的部分record[i - 7]
        # 如果失去部分是present，则更新滑窗内present次数
        if i >= 7:
            if "present" == record[i - 7]: present -= 1

        # 当前的考勤记录
        curRecord = record[i]

        if "absent" == curRecord:
            absent += 1
            if absent > 1: return "false"  # 缺勤超过1次，则拿不到全勤奖
        elif curRecord in late_leaveearly and preRecord in late_leaveearly:
            return "false"  # 连续的迟到/早退，则拿不到全勤奖
        elif "present" == curRecord:
            present += 1

        preRecord = curRecord

        # 任意连续7次考勤，缺勤/迟到/早退不超过3次, 相当于判断： 滑窗长度 - present次数 <= 3
        window_len = min(i + 1, 7)  # 滑窗长度
        if window_len - present > 3: return "false"

    return "true"


if __name__ == '__main__':
    n = int(input())
    records = [input().split() for _ in range(n)]

    for record in records: print(isAward(record))
