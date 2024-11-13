class Queue:
    def __init__(self):
        self.elements = []

    def length(self):
        return len(self.elements)

    def put(self, element):
        self.elements.append(element)

    def get(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop(0)

    def top(self):
        if self.length() == 0:
            return None
        return self.elements[0]

    def isExist(self, item):
        for element in self.elements:
            if element.number == item:
                return True
        return False

    def print(self):
        for i in range(self.length()):
            print(self.elements[i], end=" ")
        print()
