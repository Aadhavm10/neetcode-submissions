class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in hmap:
                return [hmap[complement], index]
            hmap[value] = index

        