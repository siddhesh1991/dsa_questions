# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    """
    linkedList =1 - 1 - 3 - 4 - 4 - 4 - 5 - 6 - 6
    op = 1 - 3 - 4 - 5 - 6
    """
    curNode = linkedList

    while curNode is not None:
        nextNode = curNode.next

        while nextNode is not None and curNode.value == nextNode.value:
            curNode.next = nextNode.next
            nextNode = nextNode.next

        curNode = nextNode 
            
    return linkedList
