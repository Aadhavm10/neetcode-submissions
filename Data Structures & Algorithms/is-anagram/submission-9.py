
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        smap = defaultdict(int)
        for i in s:
            smap[i] += 1

        tmap = defaultdict(int)
        for i in t:
            tmap[i] += 1

        return smap == tmap


        