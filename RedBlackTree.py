class RBTree:
    class Red:
        pass
    class Black:
        pass

    class Node:
        color = None
        value = None

        left = None
        right = None

        def __init__(self,val):
            self.color = self.Red
            self.value = val
        def Recolor(self,_color):
            self.color = _color

    root = None

    def Insert(self, X):
        self.TreeInsert(X=X)
        while X != self.root.value and self.Parent(X).color == self.Red:
            if self.Parent(X) == self.Parent(self.Parent(X).value):
                pass
            elif x == self.Parent(X).right:
                #case 2
    def Parent(self,X, pointer):
        if pointer == None:
            pointer = self.head
        if pointer.value == X:
            return None
        if pointer.left.value == X or pointer.right.value == X:
            return pointer
        if pointer.value > X:
            if pointer.left.value < X:
                return None
            self.Parent(X,pointer.left)
        else:
            if pointer.right.value < X:
                return None
            self.Parent(X,pointer.right)

    def TreeInsert(self,X,pointer):
        if pointer == None:
            pointer = self.root

        if pointer.value > X:
            if pointer.left != None:
                self.TreeInsert(X,pointer.left)
            else:
                pointer.left = self.Node(X)
                return
        else:
            if pointer.right != None:
                self.TreeInsert(X,pointer.right)
            else:
                pointer.right = self.Node(X)
                return

    def Recolor(self):
        pass
    def LeftRotate(self,A):
        pass
    def RightRotate(self,A):
        pass

#tree = RBTree
#tree.Insert(1)

class SimpleList:
    class node:
        value = None
        next = None
        previous = None

        def __init__(self,_value):
            self.value = _value

    head = None
    last = None

    def Insert(self, value):
        if self.head == None:
            self.head = self.last = self.node(value)
            return

        self.last.next = self.node(value)
        self.last.next.previous = self.last
        self.last = self.last.next

    def Print(self):
        if self.head == None:
            print 'List is empty'

        pointer = self.head
        while pointer != None:
            print pointer.value
            pointer = pointer.next

    def Test(self):
        sl = SimpleList()
        sl.Insert(4)
        sl.Insert(1)
        sl.Insert(2)
        sl.Print()