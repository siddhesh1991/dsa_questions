# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        
    def peek(self):
        # Write your code here.
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
        self.stack.append(number)

    def getMin(self):
        # Write your code here.
        return min(self.stack)

    def getMax(self):
        # Write your code here.
        return max(self.stack)


class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack =[]

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minStack.pop()
        self.maxStack.pop()
        return self.stack.pop()

    
    def push(self, number):

        if len(self.stack) == 0 :
            self.minStack.append(number)
            self.maxStack.append(number)
        else:
            current_min = min(self.minStack[-1],number)
            self.minStack.append(current_min)

            current_max = max(self.maxStack[-1],number)
            self.maxStack.append(current_max)
        
        self.stack.append(number)

    def getMin(self):
        return self.minStack[-1]

    def getMax(self):
        return self.maxStack[-1]
