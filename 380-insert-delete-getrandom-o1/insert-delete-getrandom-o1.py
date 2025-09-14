class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dct = {}

    def insert(self, val: int) -> bool:
        if val in self.dct :
            return False
        self.lst.append(val)
        self.dct[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dct :
            return False
        idx = self.dct[val]
        self.lst[idx] = self.lst[-1]
        self.dct[self.lst[-1]] = idx
        self.lst.pop()
        del self.dct[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()