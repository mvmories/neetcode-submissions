class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = True
        if s[0] == "]" or s[0] == "}" or s[0] == ")":
            return False
        
        if len(s) % 2 != 0:
            return False 
         
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[" and i == 0 or i % 2 != 0:
                print("hey")
                stack.append(s[i])
            elif s[i] == ")" and len(stack) > 0 and stack[-1] == "(" and i == 0 or i % 2 == 0:
                stack.pop()
            elif s[i] == "}" and len(stack) > 0 and stack[-1] == "{" and i == 0 or i % 2 == 0:
                stack.pop()
            elif s[i] == "]" and len(stack) > 0 and stack[-1] == "[" and i % 2 == 0:
                stack.pop()
            else: 
                valid = False        
        return valid

