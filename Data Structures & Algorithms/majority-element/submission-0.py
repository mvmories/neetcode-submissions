class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrences = {} # {5: 4, 1: 3} 
        
        for num in nums:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1
            
            if occurrences[num] > len(nums)/2:
                return num
        
        return 0