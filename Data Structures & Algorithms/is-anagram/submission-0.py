class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_ana = {}
        t_ana = {}

        for i in range(0,len(s)):
            if s[i] not in s_ana:
                s_ana[s[i]] = 0
            else:
                s_ana[s[i]] += 1
            
            if t[i] not in t_ana:
                t_ana[t[i]] = 0
            else:
                t_ana[t[i]] += 1
        
        if s_ana == t_ana:
            return True
        else:
            return False