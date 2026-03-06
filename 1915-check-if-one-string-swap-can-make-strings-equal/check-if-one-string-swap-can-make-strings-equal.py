class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        count=0
        f=s=None
        for i in range(0,len(s1)):
            if s1[i]==s2[i]:
                continue
            count+=1
            s=f
            f=i
            if (count>2):
                return False
        if (f == None and s== None):
                return True
        if (s== None):
                return False
        if (s1[s]== s2[f] and s1[f]== s2[s]):
                return True
        return False