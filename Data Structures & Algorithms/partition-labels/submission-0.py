# gurantees
# - lowercase english letters

# goal
# - We want to split the string into as many substrings as possible
# - While ensuring that each letter appears in at most one substring

# return a list of integers representing the size of these substrings in the order they appear 

# dsa
# - we want an optimum: max number of substrings
# -- fewest chars in each substring possible
# -- if we run into a char thats already been considered, we need to expand that substring to follow the rules

# -- i would be inclined to say dp and when we say dp we must ask: can greedy do it?

# -- char : substr length w/ that letter? if we encounter a char in the hashmap already, remove other letter values in hash map and consolidate them into the char we just checked hashmap

# precompute last index:
# xyzbisl
# x: 3
# y: 4
# z: 7
# b: 9
# i: 10
# s: 11
# l: 12

# if we have the last index of each, we can traverse and until we hit a last occurrence index, we know we must include all characters up to that point in the latest occurrence of those characters?
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {}
        for char in s:
            if char in last_indexes:
                continue
            last_indexes[char] = s.rfind(char)
        print(last_indexes)
        
        out, curr_substr = [], []
        partition_end = 0
        for i, char in enumerate(s):
            partition_end = max(partition_end, last_indexes[char])
            curr_substr.append(char)
            if i == partition_end:
                out.append(len(curr_substr))
                curr_substr.clear()
        return out