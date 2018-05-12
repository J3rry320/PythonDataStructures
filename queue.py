class queue:
    def __init__(self):
        self.Queue=[]
    def enqueue(self,item):
        self.Queue.append(item)
    def dequeue(self):
        data=self.Queue[0]
        del self.Queue[0]
        return data
    def peek(self):
       return self.Queue[0]
    def sizeOfQueue(self):
        return len(self.Queue)
    def isEmpty(self):
        return self.Queue==[]
    def maxElement(self):
        return max(self.Queue)

myqueue=queue()
myqueue.enqueue(134)
myqueue.enqueue(114)
myqueue.enqueue(1324)
print (myqueue.dequeue(),myqueue.peek(),myqueue.sizeOfQueue())
print(myqueue.isEmpty())
print(myqueue.maxElement())