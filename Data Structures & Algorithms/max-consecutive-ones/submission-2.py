class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # return the max number of consecutive 1's
        output = 0
        curr_best = 0
        for num in nums:
            if num == 1:
                curr_best += 1
            elif num == 0:
                output = curr_best
                curr_best = 0
            
            if output < curr_best:
                output = curr_best
                
        return output