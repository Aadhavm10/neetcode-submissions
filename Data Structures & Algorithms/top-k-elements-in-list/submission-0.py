from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create a map that is key(num) and value: how often
        for num in nums:
            count[num] = 1 + count.get(num, 0) #add values to the map
        freq = [[] for i in range(len(nums) + 1)] # create list of lists (buckets)
        for num, cnt in count.items():
            freq[cnt].append(num) #freq[1] = 3...

        res = []
        for i in range(len(freq) - 1, 0, -1): #for values of freq from big to small
            for num in freq[i]: # get the values themsevles
                res.append(num)
                if len(res) == k:
                    return res

             
