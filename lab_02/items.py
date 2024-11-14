from enum import Enum


class Label(Enum):
    OPEN = 0
    CLOSE = 1


class Node:
    def __init__(self, number: int, flag: int = Label.OPEN):
        self.number = number
        self.flag = flag

    def __str__(self):
        res = f'{self.number}'
        return res

    def __repr__(self):
        res = f'{self.number}'
        return res


class Rule:
    def __init__(
        self, 
        number: int, 
        out_node: Node, 
        node_arr: list[Node], 
        label=Label.OPEN
    ):
        self.number = number
        self.out_node = out_node
        self.node_arr = node_arr  # массив входных вершин, связанных связкой И
        self.label = label  # открытое/закрытое
