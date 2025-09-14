class RandomizedSet:

    def __init__(self):
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.lst :
            return False
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lst :
            return False
        self.lst.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()