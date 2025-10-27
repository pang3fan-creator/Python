# Dynamic programming.
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j][1] < nums[i][1] and nums[j][0] < nums[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]


if __name__ == '__main__':
    nums = [[16, 15], [13, 12], [15, 14]]
    nums = sorted(nums, key=lambda x: (x[0], x[1]), reverse=False)
    print(Solution().lengthOfLIS(nums))
