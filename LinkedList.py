class node(object):
    def _init_(self,data):
        self.data=data
        self.nextNode=None

class linkedList(object):
    def _init_(self):
        self.head=None
        self.size=0
    def insertAtStart(self,data):
        self.size=self.size+1
        newNode=node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode
    def remove(self,data):
        self.size=self.size-1
        currentNode=self.head
        previousNode=None
    while currentNode.data!=data:
        previousNode=currentNode
        currentNode=currentNode.nextNode
