class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def target_time(car):
            return (target-car[0])/car[1]

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars = sorted(cars)[::-1]
        
        stack = []
        for car in cars:
            if not stack or target_time(car) > target_time(stack[-1]):
                stack.append(car)
            
        return len(stack)

    