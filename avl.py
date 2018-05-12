class Node(object):
    def __init__(self,data):
        self.data=data
        self.height=0
        self.leftNode=None
        self.rightNode=None
class AVL(object):
    def __init__(self,data):
        self.root=None
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
        node.height=max(self.calculateHeight(node.leftNode)-self.calculateHeight(node.rightNode))+1
        tempNode.height=max(self.calculateHeight(node.leftNode)-self.calculateHeight(node.rightNode))+1
        return tempNode
    def rotateLeft(self,node):
        print("rotating left")
        tempNode=node.rightNode
        t=tempNode.leftNode
        tempNode.leftNode=node
        node.rightNode=t
        node.height=max(self.calculateHeight(node.leftNode)-self.calculateHeight(node.rightNode))+1
        tempNode.height=max(self.calculateHeight(node.leftNode)-self.calculateHeight(node.rightNode))+1
        return tempNode
