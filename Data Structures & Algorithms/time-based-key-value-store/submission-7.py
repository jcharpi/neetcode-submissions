class TimeMap:

    def __init__(self):
        self.entries = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.entries[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.entries[key]
        low, high = 0, len(timestamps) - 1
        out = ""
        while low <= high:
            mid = (low + high) // 2

            if timestamp >= timestamps[mid][0]:
                out = timestamps[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        
        return out