class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceToCenter(coords: List[int]):
            x, y = coords
            return math.sqrt(x**2 + y**2)
        
        # quick sort with final distance to center as pivot?
        def quickSort(arr, start, end):
            if end - start + 1 <= 1:
                return arr

            pivot = arr[end]
            slow = start

            for fast in range(start, end):
                if distanceToCenter(arr[fast]) < distanceToCenter(arr[end]):
                    temp = arr[slow]
                    arr[slow] = arr[fast]
                    arr[fast] = temp
                    slow += 1
            
            arr[end] = arr[slow]
            arr[slow] = pivot

            quickSort(arr, start, slow - 1)
            quickSort(arr, slow + 1, end)

            return arr
        
        return quickSort(points, 0, len(points) - 1)[:k]

                
