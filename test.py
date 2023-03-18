'''Create nodes
Create linked list
Add nodes to linked list
Print linked list'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None        

class LinkedList:
    def __init__(self):
        self.head = None
        print(self)#
        
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            # self.head.next = newNode
            lastNode = self.head
            print(lastNode)#
            while True:
                if lastNode.next is None:
                    print(lastNode.next)#
                    break
                lastNode = lastNode.next
                print(lastNode)#
            lastNode.next = newNode
            print(lastNode.next)#

    def printlist(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        print(currentNode)
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next



node1 = Node("komal")
ll = LinkedList()
ll.insert(node1)

node2 = Node("kashish")
ll.insert(node2)

node3 = Node("monika")
ll.insert(node3)

ll.printlist()