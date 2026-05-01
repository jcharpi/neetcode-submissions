class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store in hm value: frequency
        # then for each freq, store value
        hm = {}
        freq_arr = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        
        for val, freq in hm.items():
            freq_arr[freq].append(val)

        out = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                out.append(num)
                if len(out) == k:
                    return out