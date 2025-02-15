class Queue():
    def __init__(self):
        self.elements = []
    def isEmpty(self):
        return self.elements == []
    def enqueue(self,element):
        self.elements.insert(0,element)
    def dequeue(self):
        return self.elements.pop()
    def size(self):
        return len(self.elements)
myQueue = Queue()
print(myQueue.isEmpty())
