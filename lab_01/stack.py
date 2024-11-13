class Stack:
    def __init__(self):
        self.elements = []

    def length(self):
        return len(self.elements)

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.length() == 0:
            return None
        return self.elements.pop()

    def peek(self):
        element = self.pop()
        self.push(element)
        return element

    def isExist(self, item):
        isFound = False
        tempStack = Stack()

        while self.length() != 0:
            element = self.pop()
            tempStack.push(element)

            if element == item:
                isFound = True
                break
            
        while tempStack.length() != 0:
            self.push(tempStack.pop())

        return isFound
    
    def print(self):
        for i in range(self.length()):
            print(self.elements[i], end=" ")
        print()

    def show(self):
        tempStack = Stack()
        while self.length() != 0:
            tempStack.push(self.pop())

        while tempStack.length() != 0:
            element = tempStack.pop()
            if tempStack.length() != 0:
                print(f'{element} -> ', end='')
            else:
                print(f'{element}')
