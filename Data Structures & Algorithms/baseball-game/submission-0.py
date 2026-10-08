class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i, val in enumerate(operations):
            if val == "+":
                stack.append(stack[-1] + stack[-2])
            
            elif val == "C":
                stack.pop()
            
            elif val == "D":
                stack.append(stack[-1] * 2)
            
            else:
                stack.append(int(val))
        
        total = sum(stack)
        return total


