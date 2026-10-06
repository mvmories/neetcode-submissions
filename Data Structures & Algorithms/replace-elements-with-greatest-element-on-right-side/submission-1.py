class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        n = len(arr) - 1

        for i in range(n, -1, -1):
            # only last item
            # i = 5
            # arr[i] = 2
            # since its last item, save val to greatest and update arr[i] to -1
            if i == n:
                temp = arr[i]
                arr[i] = greatest
                greatest = temp
                continue
            
            # i = 2
            # arr[i] = 5
            # greatest = 3

            temp = arr[i] # 5
            # replace item with greatest from right
            arr[i] = greatest # 3
            
            # update greatest with biggest value
            if temp > greatest:
                greatest = temp # 5
            
        return arr
