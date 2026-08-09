class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        y = {}
        for i in s:
            if i in h:
                h[i] +=1
            else:
                h[i] =1
        for j in t:
            if j in y:
                y[j] +=1
            else:
                y[j] =1
        if len(h) == len(y):
            for k in h:
                if k in y and h[k] == y[k]:
                    pass
                else: 
                    return False
        else:
            return False
        return True

        
        