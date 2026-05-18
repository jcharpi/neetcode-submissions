class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)

    def validTimestamp(self, timestamp, key, m):
        return timestamp >= self.timestamps[key][m][0]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.timestamps[key]) - 1
        out = ""
        while l <= r:
            m = (l + r) // 2

            if self.validTimestamp(timestamp, key, m):
                out = self.timestamps[key][m][1]
                l = m + 1
            else:
                r = m - 1
        
        return out