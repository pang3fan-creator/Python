import sys

line_num = 0
sings_num = int(input())
op_str = input()
all_num = [i for i in range(sings_num + 1)]
all_num = all_num[1:]
left = 0
right = min(3, sings_num - 1)
screen_pos = 0
for s in op_str:
    if s == 'U':
        if left == 0 and screen_pos == 0:
            left = max(0, sings_num - 4)
            right = sings_num - 1
            screen_pos = min(3, sings_num - 1)
        elif screen_pos > 0:
            screen_pos -= 1
        else:
            left -= 1
            right -= 1
    elif s == 'D':
        if right == sings_num - 1 and screen_pos == min(3, sings_num - 1):
            left = 0
            right = min(3, sings_num - 1)
            screen_pos = 0
        elif screen_pos < min(3, sings_num - 1):
            screen_pos += 1
        else:
            left += 1
            right += 1
output_str = ''
screen_pos = left + screen_pos
while left <= right:
    output_str += str(all_num[left])
    output_str += ' ' if left != right else '\n'
    left += 1
output_str += str(all_num[screen_pos])
print(output_str)
