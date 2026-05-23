class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left, right = arr[l:m + 1], arr[m + 1:r + 1]
            
            i = l
            j = k = 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                i += 1
                j += 1
            
            while k < len(right):
                arr[i] = right[k]
                i += 1
                k += 1
                        
        def mergeSort(arr, start, end):
            if end - start + 1 <= 1:
                return arr

            mid = (start + end) // 2

            mergeSort(arr, start, mid)
            mergeSort(arr, mid + 1, end)

            merge(arr, start, mid, end) 
            return arr
        
        return mergeSort(nums, 0, len(nums) + 1)