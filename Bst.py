class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
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
            print("inorder")
            self.traverseInOrder(self.root)
            print("postOrder")
            self.traversePostOrder(self.root)
            print("preorder")
            self.traversePreOrder(self.root)
    def traverseInOrder(self,node):
        if node.leftchild:
            self.traverseInOrder(node.leftchild)
        print(node.data)
        if node.rightchild:
            self.traverseInOrder(node.rightchild)
    def traversePostOrder(self,node):
        if node.leftchild:
            self.traversePostOrder(node.leftchild)
        if node.rightchild:
            self.traversePostOrder(node.rightchild)
        print(node.data)
    def traversePreOrder(self,node):
        print(node.data)
        if node.leftchild:
            self.traversePreOrder(node.leftchild)
        if node.rightchild:
            self.traversePreOrder(node.rightchild)
    def remove(self,data):
        if self.root:
            self.root=self.removeNode(data,self.root)  
    def removeNode(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.leftchild=self.removeNode(data,node.leftchild)
        elif data>node.data:
            node.rightchild=self.removeNode(data,node.rightchild)
        else:
            if not node.leftchild and node.rightchild:
                print("removing a leaf node")
                del node
                return None
            if not node.leftchild:
                print("delete with a single right child")
                tempNode=node.rightchild
                del node
                return tempNode
            elif not node.rightchild:
                print("delete with a single left child")
                tempNode=node.leftchild
                del node
                return tempNode
            print("removing a node with both children")
            tempNode=self.getPredecessor(node.leftchild)
            node.data=tempNode
            node.leftchild=self.removeNode(tempNode.data,node.leftchild)
        return node
    def getPredecessor(self,node):
        if node.rightchild:
            return self.getPredecessor(node.rightchild)
        return node
   
bst=BinaryTree()
bst.insert(1323)
bst.insert(12)
bst.insert(29)
bst.insert(7)
bst.insert(232)
bst.insert(111)
bst.insert(1123231)
bst.insert(13224411)
print(bst.findMin())
print(bst.findmax())
bst.traverse()
bst.remove(7)


print(bst.findmax())
bst.traverse()