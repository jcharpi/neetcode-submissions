class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keys: 0-len of array
        # values: numbers that occur that many times

        # keys: number, values: occurrences
        # 7: 2
        # for 
        count = {}
        freq = [[] for i in range (len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for n, c in count.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
        