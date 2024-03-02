# @YasmineGha
class TimeMap:

    def __init__(self):
        # Initialize an empty dictionary to store key-value pairs
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.dic[key] = self.dic.get(key,[]) + [[value,timestamp]] -> This takes O(n)
        # If the key is not in the dictionary, create a new list for it.
        # Otherwise, append the new value & timestamp to the existing list -> This takes O(1)
        self.dic[key].append((value, int(timestamp)))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # If the key is not in the dictionary, return an empty string
        if key not in self.dic :
            return res
        else :
            # Retrieve the list of values and timestamps for the key
            pairs = self.dic.get(key, [])
            # If there's only one pair and its timestamp is <= to the given timestamp,
            # return its value
            if len(pairs) == 1 and pairs[0][1] <= timestamp :
                return pairs[0][0]
            # If the given timestamp is < the first timestamp in the list,
            # return an empty string because there's no valid value for this timestamp
            if timestamp < self.dic[key][0][1] :
                return res
            # use binary search to find the value with the largest timestamp that is <= to the given timestamp
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

'''
# Naive approach
for p in range(len(pairs)-1,-1,-1):
    v = pairs[p][0]
    t = pairs[p][1]
    if t <= timestamp:
        return v
    else:
        return ""
'''