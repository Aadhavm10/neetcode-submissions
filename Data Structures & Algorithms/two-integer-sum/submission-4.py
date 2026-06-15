class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for index,val in enumerate(nums):
            complement = target - val
            if complement in hmap:
                return [hmap[complement], index]
            hmap[val] = index


        