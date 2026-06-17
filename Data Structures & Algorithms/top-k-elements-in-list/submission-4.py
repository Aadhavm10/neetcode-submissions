from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        buckets = [[] for i in range(len(nums)+ 1)]
        for num, index in count.items():
            buckets[index].append(num)

        output = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output


        
        