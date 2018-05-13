class Node(object):
    def __init__(self,data):
        self.data=data
        self.height=0
        self.leftNode=None
        self.rightNode=None
class AVL(object):
    def __init__(self,data):
        self.root=None
    def insert(self,data):
        self.root=self.insertNode(data,self.root)
    def insertNode(self,data,node):
        if not node:
            return Node(data)
        if data<node.data:
            node.leftNode=self.insertNode(data,node.leftNode)
        elif data>node.data:
            node.rightNode=self.insertNode(data,node.rightNode)
        height=max(self.calculateHeight(node.leftNode),self.calculateHeight(node.rightNode))+1
        return self.checkViolation(data,node)
    def checkViolation(self,data,node):
        balance=self.checkBalance(node)
        if balance>1 and data<node.leftNode.data:
            print("Left Left heavy situatuon")
            return self.rotateRight(node)
        elif balance<1 and data>node.rightNode.data:
            print("right right heavay situation")
            return self.rotateLeft(node)

    def calculateHeight(self,node):
        if not node:
            return -1
        return node.height
    def checkBalance(self,node):
        if not node:
            return 0
        return self.calculateHeight(node.leftNode)-self.calculateHeight(node.rightNode)#If the value >1 it is a left heavy tree if it is <-1 it is right heavy situation if it is between 0 and 1 it is balnced 
    def rotateRight(self,node):
        print("Rotating Right")
        tempNode=node.leftNode
        t=tempNode.rightNode
        tempNode.rightNode=node
        node.leftNode=t
        node.height=max(self.calculateHeight(node.leftNode),self.calculateHeight(node.rightNode))+1
        tempNode.height=max(self.calculateHeight(node.leftNode),self.calculateHeight(node.rightNode))+1
        return tempNode
    def rotateLeft(self,node):
        print("rotating left")
        tempNode=node.rightNode
        t=tempNode.leftNode
        tempNode.leftNode=node
        node.rightNode=t
        node.height=max(self.calculateHeight(node.leftNode),self.calculateHeight(node.rightNode))+1
        tempNode.height=max(self.calculateHeight(node.leftNode),self.calculateHeight(node.rightNode))+1
        return tempNode
