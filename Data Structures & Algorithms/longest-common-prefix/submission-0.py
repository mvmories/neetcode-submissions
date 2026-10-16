class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            # shrink until prefix of s 
            while not s.startswith(prefix):
                # complete prefix except last char
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix