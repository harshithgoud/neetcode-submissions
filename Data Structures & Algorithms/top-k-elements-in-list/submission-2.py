class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        res = []
        for num in nums:
            if num in hmap:
                hmap[num] +=1
            else:
                hmap[num] = 1      
        return list(dict((sorted(hmap.items(),key=lambda item: item[1], reverse = True))).keys())[:k]
            

            