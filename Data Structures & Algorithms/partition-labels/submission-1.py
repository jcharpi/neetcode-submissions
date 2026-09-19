class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {}
        for i, char in enumerate(s):
            last_indexes[char] = i

        out = []
        curr_substr_count = partition_end = 0
        for i, char in enumerate(s):
            partition_end = max(partition_end, last_indexes[char])
            curr_substr_count += 1
            if i == partition_end:
                out.append(curr_substr_count)
                curr_substr_count = 0
        return out