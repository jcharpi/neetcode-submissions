class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time_to_target(car):
            return (target - car[0]) / car[1]

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)

        stack = []
        for car in cars:
            if not stack or time_to_target(car) > time_to_target(stack[-1]):
                stack.append(car)
        
        return len(stack)