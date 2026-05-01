class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[pos, speed] for pos, speed in zip(position, speed)]
        stack = []

        pairs.sort()

        def timeToEnd(pos, speed):
            return (target -  pos) / speed

        for i in range(len(pairs) - 1, -1, -1):
            car = pairs[i]
            if not stack or timeToEnd(car[0], car[1]) > stack[-1]:
                stack.append(timeToEnd(car[0], car[1]))
        return len(stack)
                 
