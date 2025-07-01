class Node :
    def __init__(self, key, val) :
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.nxt = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key in self.cache :
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity :
            lru = self.oldest.nxt
            self.remove(lru)
            del self.cache[lru.key]
    
    def remove(self, node) :
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def insert(self, node) :
        prev, nxt = self.latest.prev, self.latest
        prev.nxt = nxt.prev = node
        node.nxt = nxt
        node.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)