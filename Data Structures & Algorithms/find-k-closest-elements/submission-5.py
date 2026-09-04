# You are given a sorted integer array arr

# You are given two integers k and x

# return the k closest integers to x in the array

# arr.length = medium
# arr[i] = medium

# what do we know for sure?
# - The closest numbers are always consecutive bc we have sorted order
# - we care about the numbers we are considering
# - we always have a fixed size window

# - fixed size sliding window
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def isCloser(a, b):
            return (abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b))

        left, window = 0, deque()
        for right in range(len(arr)):
            if len(window) < k:
                window.append(arr[right])
            elif isCloser(arr[right], window[0]):
                window.popleft()
                window.append(arr[right])
                left += 1
            
        return list(window)