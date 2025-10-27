import json

if __name__ == '__main__':
    nums = json.loads(input())
    k = int(input())
    nums_max = []
    for i in range(len(nums) - k + 1):
        num_max = max(nums[i:i + k])
        nums_max.append(num_max)
    print(nums_max)
