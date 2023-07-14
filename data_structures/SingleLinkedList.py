class Node:
  def __init__(self,value = None):
    self.data = value
    self.next = None

# works with referencing memory thats the whole play
class LinkedList:
  def __init__(self,value = None):
    self.head = Node(value)
    self.tail = self.head
    self.length = 1

  def append(self,value):
    newNode = Node(value)
    self.tail.next = newNode
    self.tail = newNode
    self.length += 1

  def prepend(self,value):
    newNode = Node(value)
    newNode.next = self.head
    self.head = newNode  
    self.length += 1

  def insert(self,index,value):
    
    if index >= self.length:
      return self.append(value)
    if index == 0:
      return self.prepend(value)

    newNode = Node(value)

    i = 0
    curNode = self.head
    while i != index-1:#i != index:
      #prevNode = curNode
      curNode = curNode.next
      i +=1 

    newNode.next = curNode.next
    curNode.next = newNode

    # newNode.next = curNode
    # prevNode.next = newNode
    self.length += 1

    def printList(self):
	    temp = self.head
	    while (temp):
		    print (temp.data)
		    temp = temp.next

    def remove(self,index):
    
        if index == 0:
            self.head = self.head.next
        else:
          i = 0
        curNode = self.head
        while i != index-1:
            prevNode = curNode
            curNode = curNode.next
        i +=1 

      prevNode.next = curNode.next

    self.length -= 1


#   reverse() {
#       if (!this.head.next) {
#         return this.head;
#       }
#       let first = this.head;
#       this.tail = this.head;
#       let second = first.next;
  
#       while(second) {
#         const temp = second.next;
#         second.next = first;
#         first = second;
#         second = temp;
#       }
  
#       this.head.next = null;
#       this.head = first;
#       return this.printList();
#     }


l1 = LinkedList(10)
l1.append(2)
l1.append(5)
l1.printList()
l1.prepend(2)
l1.prepend(5)
l1.printList()
l1.insert(2,33)
l1.insert(3,43)
l1.printList()
l1.insert(0,33)
l1.insert(99,43)
l1.printList()
l1.remove(3)
l1.printList()