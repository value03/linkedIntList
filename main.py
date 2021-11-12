class LinkedIntList:


    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None


    def addLast(self,value):
        if self.first == None:
            self.last = IntNode(value, None)
            self.first = self.last
        else:
            node = IntNode(value, None)
            self.last.next = node
            self.last = node
        self.size += 1


    def addFirst(self, value):
        self.first = IntNode(value, self.first)
        self.size += 1


    def removeFirst(self):
        if self.isEmpty:
            raise ReferenceError("list is empty")

        self.first = self.first.next
        self.size -= 1
    

    def removeLast(self):
        if self.isEmpty:
            raise ReferenceError("list is empty")

        currentnode = self.first

        while currentnode.next != self.last:
            currentnode = currentnode.next

        currentnode.next = None
        self.size -= 1


    def clear(self):
        self.size = 0
        self.first = None
        self.last = None


    def isEmpty(self):
        if self.last == None:
            return True
        else:
            return False


    def get(self, index):
        if index >= self.size:
            raise ValueError("indexOutOfBounds")

        currentnode = self.first
        for i in range(index):
            currentnode = currentnode.next
        return currentnode.value


    def set(self, index, value):
        if index >= self.size:
            raise ValueError("indexOutOfBounds")

        currentnode = self.first
        for i in range(index):
            currentnode = currentnode.next
        currentnode.value = value


    def printList(self):
        string = "["
        currentnode = self.first
        while True:
            string += " {}".format(currentnode.value)
            if currentnode.next == None:
                break
            else:
                currentnode = currentnode.next

        string += " ]"

        return string

class IntNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next


newList = LinkedIntList()

newList.addLast(5)
newList.addLast(6)
newList.addFirst(2)
newList.addFirst(8)
newList.addLast(17)

print(newList.size)
print(newList.first.value)
print(newList.last.value)
print(newList.printList())
