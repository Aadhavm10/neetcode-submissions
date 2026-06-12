class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: 
            return nums[0]

        def helper(nums):
            n = len(nums)
            if not nums:
                return 0
            if n == 1:
                return nums[0]

            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(dp[0],nums[1])

            for i in range(2,n):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
            return dp[n-1]
        
        scenario1 = helper(nums[1:])
        scenario2 = helper(nums[0 :-1])
        return max(scenario1, scenario2)

        