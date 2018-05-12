class stack:
    def __init__(self):
        self.stackarr=[]
    def isEmpty(self):
        return self.stackarr==[]
    def push(self,item):
        self.stackarr.append(item)
    def pop(self):
        data=self.stackarr[-1]
        del self.stackarr[-1]
        return data
    def peek(self):
        data=self.stackarr[-1]
        return data
    def sizeOfArray(self):
        return len(self.stackarr)
myStack=stack()
myStack.push(12)
myStack.push(13)
myStack.push(123)
myStack.push(1244)
myStack.push(621)
empty=myStack.isEmpty()

poppedElement=myStack.pop()
topElement=myStack.peek()
print(myStack.isEmpty(),topElement,poppedElement)
print(myStack.sizeOfArray())
print(empty)