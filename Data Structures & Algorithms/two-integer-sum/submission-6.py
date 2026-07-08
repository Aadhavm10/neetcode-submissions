from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = defaultdict(int)
        for i, num in enumerate(nums):
            j = target - num
            if j in hmap: #found
                return [hmap[j], i]
            hmap[num] = i

        