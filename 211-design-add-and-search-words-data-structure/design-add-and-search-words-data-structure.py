class Node(Dict) :
    def __init__(self) :
        self.ends = False

class WordDictionary:

    def __init__(self):
        self.node = Node()

    def addWord(self, word: str) -> None:
        node = self.node

        for char in word :
            if char not in node.keys() :
                node[char] = Node()
            
            node = node[char]
        
        node.ends = True
        

    def search(self, word: str) -> bool:
        return self.mysearch(word, self.node)

    def mysearch(self, word, node) :
        for idx in range(len(word)) :
            char = word[idx]

            if char == '.' :
                rtn = False
                for my_char in node.keys() :
                    rtn = rtn or self.mysearch(word[idx + 1 :], node[my_char])
                
                return rtn

            else :
                if char in node.keys() :
                    node = node[char]
                else :
                    return False

        return node.ends


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)