class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for index, item in enumerate(nums):
            if item in hm:
                return [hm[item],index]
            else:
                hm[target-item] = index
        print(hm)
        # key: needed num
        # value: index
        # if curr in keys, return index, curr index 

        