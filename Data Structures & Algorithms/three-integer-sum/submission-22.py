class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []

        # Sort the array first
        sortedNums = sorted(nums)

        # Use three nested loops conceptually: outer loop for fixed element, two pointers for the other two
        for i in range(len(sortedNums)):
            # Skip duplicates in the outer loop
            if i != 0 and sortedNums[i] == sortedNums[i-1]:
                continue

            l, r = i + 1, len(sortedNums) - 1
            while l < r:
                # Move pointers based on sum comparison (too small/too large)
                if sortedNums[l] + sortedNums[r] + sortedNums[i] > 0:
                    r -= 1
                elif sortedNums[l] + sortedNums[r] + sortedNums[i] < 0:
                    l += 1
                else:
                    out.append([sortedNums[l], sortedNums[r], sortedNums[i]])
                    
                    l += 1
                    r -= 1

                    # Skip duplicates for both pointers after finding a valid triplet
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1
                    while l < r and sortedNums[r] == sortedNums[r + 1]:
                        r -= 1
        return out
