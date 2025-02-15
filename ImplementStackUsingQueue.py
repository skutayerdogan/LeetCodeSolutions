from collections import deque


class MyStack:

    def __init__(self):
        self.Myqueue = deque()

    def push(self, x: int) -> None:
        self.Myqueue.append(x)
    def pop(self) -> int:
        counter = 0
        for i in range(0,len(self.Myqueue)-1):
            num = self.Myqueue.popleft()
            self.Myqueue.append(num)
        return self.Myqueue.popleft()
    def top(self) -> int:
        return self.Myqueue[-1]

    def empty(self) -> bool:
        return  len(self.Myqueue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(3)
print(obj.empty())
print(obj.top())