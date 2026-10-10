class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        valid = True
        for i in range(1, n//2):
            if s[i-1] == "(" and s[-i] == ")":
                continue
            elif s[i-1] == "{" and s[-i] == "}":
                continue
            elif s[i-1] == "[" and s[-i] == "]":
                continue
            else:
                valid = False
        return valid

