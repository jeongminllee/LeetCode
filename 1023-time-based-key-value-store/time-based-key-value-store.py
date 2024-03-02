class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic :
            self.dic[key] = [(value, timestamp)]
        else :
            self.dic[key].append((value, int(timestamp)))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.dic :
            return res
        else :
            pairs = self.dic.get(key, [])

            if len(pairs) == 1 and pairs[0][1] <= timestamp :
                return pairs[0][0]

            if timestamp < self.dic[key][0][1] :
                return res

            left, right = 0, len(pairs) - 1

            while left <= right :
                mid = (left + right) // 2
                if pairs[mid][1] > timestamp :
                    right = mid - 1
                else :
                    res = pairs[mid][0]
                    left = mid + 1

            return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)