class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap1 = {}
        for word in strs: 
            k = ''.join(sorted(list(word)))
            if k in hmap1:
                hmap1[k].append(word)
            else:
                hmap1[k] = [word]
        return list(hmap1.values())
            
        

        
        