class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num: freq
        freq = [[] for i in range(len(nums) + 1)] # frequent: nums
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, f in count.items():
            freq[f].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                res.append(v)
                if(len(res) == k):
                    return res