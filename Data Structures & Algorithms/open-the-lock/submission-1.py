class Solution:
    def openLock(self, deadends, target):
        count = 0
        visited = set(deadends)
        if "0000" in visited:
            return -1

        queue = deque()
        queue.append("0000")
        visited.add("0000")

        while queue:
            level_count = len(queue)
            for _ in range(level_count):
                curr = queue.popleft()
                if curr == target:
                    return count
                for wheel in range(4):
                    for delta in (-1, 1):
                        neighbor = self.turn_wheel(curr, wheel, delta)
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            count += 1

        return -1

    def turn_wheel(self, curr, wheel, delta):
        wheel_digits = list(curr)
        turned_digit = (int(wheel_digits[wheel]) + delta + 10) % 10
        wheel_digits[wheel] = str(turned_digit)
        return "".join(wheel_digits)