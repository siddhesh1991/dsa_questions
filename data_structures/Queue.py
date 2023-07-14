class Node:
  def __init__(self,value = None):
    self.data = value
    self.next = None

class Queue:
  def __init__(self):
    self.first = None 
    self.last = None 
    self.length = 0

  def peek(self):
    return self.first.data

  def enqueue(self,value):
    
    newNode = Node(value)
    if self.length == 0:
      self.first = newNode
      self.last = newNode
    else:
      self.last.next = newNode
      self.last = newNode

    self.length += 1
    
  def dequeue(self):
    if self.first == None:
      return None
    
    if self.length == 0:
      self.last = None
    
    self.first = self.first.next
    self.length -= 1
