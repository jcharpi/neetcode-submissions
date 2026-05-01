class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # go through each number and count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for number, frequency in count.items():
            freq[frequency].append(number)
        
        # go through each sub array, and each item in each subarray from back to front until == k
        out = []
        for sai in range(len(freq) - 1, 0, -1):
            for num in freq[sai]:
                out.append(num)
                if len(out) == k:
                    return out