from items import Edge, Node
from queue import Queue


class GraphBFS:
    def __init__(self, edgeList: list[Edge]):
        self.edgeList = edgeList
        self.opened = Queue()
        self.closed = list()
        self.goal = None
        self.isSolutionFound = False
        self.childCounter = True
        self.resultPath = {}

    def find(self, start: int, goal: int):
        self.opened.put(Node(start))
        self.goal = goal

        while self.childCounter and not self.isSolutionFound:
            print("Очередь: ", end="")
            self.opened.print()
            
            self.childsSearch()
            if self.isSolutionFound == True:
                break

            currentNode = self.opened.get()
            self.closed.append(currentNode.number)

            if self.opened.length() != 0:
                self.childCounter = True
        
        if self.isSolutionFound == False:
            return None
        
        return self.getResultPath(start)

    def childsSearch(self):
        self.childCounter = False
        currentNode = self.opened.top()

        for edge in self.edgeList:
            if edge.startNode.number != currentNode.number \
                or edge.used \
                or self.opened.isExist(edge.endNode.number) \
                or edge.endNode.number in self.closed:
                continue

            edge.used = True
            self.opened.put(edge.endNode)
            self.resultPath[edge.endNode.number] = edge.startNode.number
            self.childCounter = True

            if edge.endNode.number == self.goal:
                self.isSolutionFound = True
                break

    def getResultPath(self, start: int):
        current = self.goal
        result = [current]
        while current != start:
            current = self.resultPath[current]
            result.append(current)

        return result
    
    @classmethod
    def showResult(cls, res: list) -> None:
        print()
        if res is not None:
            for i in range(len(res) - 1, -1, -1):
                if i != 0:
                    print(f'{res[i]} -> ', end='')
                else:
                    print(f'{res[i]}')
        else:
            print("\nНе удалось определить путь")
        print()
