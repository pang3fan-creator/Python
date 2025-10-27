def main(nums):
    max_count = 0
    for i in range(len(nums)):
        l_point, r_point, count = nums[i], nums[i], 1
        for j in range(i + 1, len(nums)):
            if nums[j] > r_point: l_point, r_point, count = r_point, nums[j], count + 1
            if l_point < nums[j] <= r_point: r_point = nums[j]
        max_count = max(max_count, count)
    return max_count


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(main(nums))
