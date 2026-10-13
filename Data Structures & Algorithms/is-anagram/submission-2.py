class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        if len(s) != len(t):
            return False
 
        for char in s:
            if char not in s_hash:
                s_hash[char] = 1
            else:
                s_hash[char] += 1
        
        for char in t:
            if char not in t_hash:
                t_hash[char] = 1
            else:
                t_hash[char] += 1

        # if len(s_hash) != len(t_hash):
        #     return False
        
        for key, val in s_hash.items():
            if key not in t_hash:
                return False
            
            if val != t_hash[key]:
                return False 
        
        return True

