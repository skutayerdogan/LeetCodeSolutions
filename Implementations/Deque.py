class Deque:
    def __init__(self):
        self.elements = []
    def isEmpty(self):
        return self.elements == []
    def addRight(self,item):
        self.elements.append(item)
    def addLeft(self,item):
        self.elements.insert(0,item)
    def removeRight(self):
        return self.elements.pop()
    def removeLeft(self):
        return self.elements.pop(0)
    def size(self):
        return len(self.elements)