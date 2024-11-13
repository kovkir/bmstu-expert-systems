class Node:
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __repr__(self):
        return f'{self.number}'


class Edge:
    def __init__(self, startNode: Node, endNode: Node):
        self.startNode = startNode
        self.endNode = endNode
        self.used = False
