class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if s[0] == "]" or s[0] == "}" or s[0] == ")":
            return False
        
        if len(s) % 2 != 0:
            return False 
         
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            if s[i] == ")":
                if len(stack) == 0:
                    return False
                if stack.pop() == "(":
                    continue
                else:
                    return False
            if s[i] == "}":
                if len(stack) == 0:
                    return False
                if stack.pop() == "{":
                    continue
                else:
                    return False
            if s[i] == "]":
                if len(stack) == 0:
                    return False
                if stack.pop() == "[":
                    continue
                else:
                    return False
                
        if len(stack) > 0:
            return False

        return True

