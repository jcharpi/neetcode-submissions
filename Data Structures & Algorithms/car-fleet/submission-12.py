class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        out = []
        cars = sorted(zip(position, speed), reverse = True)
        for position, speed in cars:
            time_to_dest = (target - position) / speed
            if not out or time_to_dest > out[-1]:
                out.append(time_to_dest)

        return len(out)