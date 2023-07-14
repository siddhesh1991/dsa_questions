
class Branch:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.key = key

  def display(self):
    lines, *_ = self._display_aux()
    for line in lines:
      print(line)
  
  def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
      line = '%s' % self.key
      width = len(line)
      height = 1
      middle = width // 2
      return [line], width, height, middle

    # Only left child.
    if self.right is None:
      lines, n, p, x = self.left._display_aux()
      s = '%s' % self.key
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
      second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
      shifted_lines = [line + u * ' ' for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
      lines, n, p, x = self.right._display_aux()
      s = '%s' % self.key
      u = len(s)
      first_line = s + x * '_' + (n - x) * ' '
      second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
      shifted_lines = [u * ' ' + line for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = self.left._display_aux()
    right, m, q, y = self.right._display_aux()
    s = '%s' % self.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
      left += [n * ' '] * (q - p)
    elif q < p:
      right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self,key):

    newBranch = Branch(key)

    if self.root is None:
      self.root = newBranch
    else:
      currentBranch = self.root # creating a referefence here then modify with reference
      while True:
        if currentBranch.key > key:
          if currentBranch.left is None:
            currentBranch.left = newBranch
            #return self
            break 
          else:
            currentBranch = currentBranch.left
        else:
          if currentBranch.right is None:
            currentBranch.right = newBranch
            #return self
            break
          else:
            currentBranch = currentBranch.right
  
  def lookup(self,key):

    if self.root is None:
      return False

    currentBranch = self.root

    while currentBranch is not None:
      if currentBranch.key == key:
        return currentBranch.display()
      elif key < currentBranch.key:
        currentBranch = currentBranch.left
      else:
        currentBranch = currentBranch.right
      
    return False

  def display(self):
    lines, *_ = self.root._display_aux()
    for line in lines:
      print(line)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.insert(21)
tree.insert(12)