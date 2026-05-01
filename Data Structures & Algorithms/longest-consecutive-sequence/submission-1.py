class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]
        
        # we sort
        
        # [2,3,4,5,10,20]

        # into hashmap
        # number: largest consecutive string
        # 2: [2], 3: [2,3], 4:[2,3,4], 5:[2,3,4,5], 10:[10], 20:[20]
        # how do we check if we start new value? not sure yet
        # then sort values, make it a list, choose the last, biggest value, get length

        sorted_nums = sorted(nums)
        out = {}
        lengths = []
        for num in sorted_nums:
            # duplicates don't really matter
            if num in out:
                continue

            if (num-1) in out:
                con_arr = out[num-1].copy()
                con_arr.append(num)
                out[num] = con_arr
            else:
                out[num] = [num]
        for arr in list(out.values()):
            lengths.append(len(arr))
        
        lengths_sorted = sorted(lengths)
        lengths_sorted.reverse()

        return lengths_sorted[0] if lengths_sorted else 0