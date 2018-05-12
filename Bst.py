class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insertRoot(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(data,self.root)
    def insertNode(self,data,node):
        if(data<node.data):
            if node.leftchild:
                self.insertNode(data,node.leftchild)
            else:
                node.leftchild=Node(data)
        else:
            if node.rightchild:
                self.insertNode(data,node.rightchild)
            else:
                node.rightchild=Node(data)
    def findMin(self):
        if self.root:
            return self.Minm(self.root)
    def Minm(self,node):
        if node.leftchild:
            return self.Minm(node.leftchild)
        return node.data
    def findmax(self):
        if self.root:
            return self.Maxm(self.root)
    def Maxm(self,node):
        if node.rightchild:
            return self.Maxm(node.rightchild)
        return node.data
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
    def traverseInOrder(self,node):
        if node.leftchild:
            traverseInOrder(node.leftchild)
        print(node.data)
        if node.rightchild:
            traverseInOrder(node.rightchild)
        print(node.data)
        
