class Node:
  def __init__(self,value = None):
    self.data = value
    self.next = None

class Stack:
  def __init__(self):
    self.top = None 
    self.bottom = None 
    self.length = 0

  def peek(self):
    return self.top.data

  def push(self,value):
    
    newNode = Node(value)
    if self.length == 0:
      self.top = newNode
      self.bottom = newNode
    else:
      newNode.next = self.top
      self.top = newNode 
    
    self.length += 1
    
  def pop(self):
    if self.top == None:
      return None
    
    if self.length == 0:
      self.bottom = None
    
    self.top = self.top.next
    self.length -= 1
