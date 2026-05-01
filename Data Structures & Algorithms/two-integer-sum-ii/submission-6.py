class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start pointers on opposite ends
        l, r = 0, len(numbers) - 1
        
        # while l + r > target, decrease r; if l+r < target, increase l
        while numbers[l] + numbers[r] != target:   
            while l < r and numbers[l]+numbers[r] > target:
                r -= 1

            while l < r and numbers[l]+numbers[r] < target:
                l += 1
            
        return [l+1, r+1]

