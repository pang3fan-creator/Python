import sys

for line in sys.stdin:
    cmds = line.strip().split()
    cmd_set = ['reset', 'reset board', 'board add', 'board delete',
               'reboot backplane', 'backplane abort', 'he he']
    ops = ['reset what', 'board fault', 'where to add', 'no board at all',
           'impossible', 'install first', 'unknown command']
    flg = False
    if len(cmds) == 1:
        if cmd_set[0].startswith(cmds[0]):
            print(ops[0])
        else:
            print(ops[-1])
    else:
        for i in range(1, len(cmd_set)):
            tmp_cmd = cmd_set[i].split()
            if tmp_cmd[0].startswith(cmds[0]) and tmp_cmd[1].startswith(cmds[1]):
                print(ops[i])
                flg = True
                break
        if not flg: print(ops[-1])
