class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Iterate through each character position of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this position across all other strings
            for s in strs[1:]:
                # If we reached the end of `s` or found a mismatch
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
                    
        return strs[0]