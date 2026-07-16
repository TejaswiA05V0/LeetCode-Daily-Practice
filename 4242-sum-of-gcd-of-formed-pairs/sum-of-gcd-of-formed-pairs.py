class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        n = len(nums)
        curMax = 0
        for i in range(n):
            curMax = max(curMax, nums[i])
            prefixGcd.append(math.gcd(nums[i], curMax))
        prefixGcd.sort()
        res = 0
        for i in range(n // 2):
            res += math.gcd(prefixGcd[i], prefixGcd[n - (i + 1)])
        return res
        