class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in sums:
                return [sums[complement], i]
            sums[n] = i