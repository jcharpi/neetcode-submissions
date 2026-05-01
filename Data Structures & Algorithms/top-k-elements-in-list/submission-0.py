class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so we want:
        # sorted keys with values of numbers (Keys: Number)
        # Where keys are number of occurrences and values are the number that occurs
        occ = {}
        for num in nums:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1
        
        sorted_occ = list(dict(sorted(occ.items(), key=lambda item: item[1], reverse=True)).keys())
        
        result = []
        for i in range(k):
            result.append(sorted_occ[i])

        return result