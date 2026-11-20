class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate_a, candidate_b = -1, -1
        count_a, count_b = 0, 0

        for num in nums:
            if num == candidate_a:
                count_a += 1
            elif num == candidate_b:
                count_b += 1
            elif count_a == 0:
                candidate_a = num
                count_a = 1
            elif count_b == 0:
                candidate_b = num
                count_b = 1
            else:
                count_a -= 1
                count_b -= 1

        count_a, count_b = 0, 0
        for num in nums:
            if num == candidate_a:
                count_a += 1
            elif num == candidate_b:
                count_b += 1

        threshold = len(nums) // 3
        result = []
        if count_a > threshold:
            result.append(candidate_a)
        if count_b > threshold:
            result.append(candidate_b)

        return result