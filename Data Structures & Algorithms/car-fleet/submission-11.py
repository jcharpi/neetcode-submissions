class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def timeToDest(target, position, speed):
            return (target - position) / speed

        out = []
        cars = sorted(zip(position, speed), reverse = True)
        for i in range(len(cars)):
            time_to_dest = timeToDest(target, cars[i][0], cars[i][1])
            if not out or time_to_dest > out[-1]:
                out.append(time_to_dest)

        return len(out)