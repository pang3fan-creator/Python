from pathlib import Path


class GameLog:
    """游戏日志类"""

    def __init__(self):
        self.logs = []
        self.path = Path('../game/logs.txt')

    def add_log(self, message):
        self.logs.append(message)
        self.save_logs_txt()

    def save_logs_txt(self):
        with open(self.path, 'a') as file:
            for log in self.logs:
                file.write(log + '\n')

    def clear_logs(self):
        with open(self.path, 'w'):
            return "日志已清空"

    def check_ranking(self):
        with open(self.path, 'r') as file:
            list_logs = file.readlines()
        for i in range(len(list_logs)):
            list_logs[i] = list_logs[i].strip().split(',')
        # if len(list_logs) <= 1:
        #     return list_logs
        for i in range(len(list_logs) - 1):
            for j in range(i + 1, len(list_logs)):
                if int(list_logs[i][-1]) > int(list_logs[j][-1]):
                    list_logs[i], list_logs[j] = list_logs[j], list_logs[i]
        return list_logs
