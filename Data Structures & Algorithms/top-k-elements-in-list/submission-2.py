from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        buckets = [[] for i in range(len(nums) + 1)]

        for i, c in count.items():
            buckets[c].append(i)

        res = []
        for i in range(len(buckets) -1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res

        

        