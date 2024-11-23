from typing import List
from enum import Enum


class Label(Enum):
    OPEN = 0
    CLOSE = 1
    FORBIDDEN = -1
    VIEWED = 2


class Node:
    def __init__(self, number: int, flag: int = Label.OPEN):
        self.number = number
        self.flag = flag

    def __str__(self):
        return f'{self.number}'

    def __repr__(self):
        return f'{self.number}'


class Rule:
    def __init__(
        self, 
        number: int, 
        out_node: Node, 
        node_arr: List[Node], 
        label=Label.OPEN
    ):
        self.number = number
        self.out_node = out_node
        self.node_arr = node_arr  # массив входных вершин, связанных связкой И
        self.label = label  # открытое/закрытое/запрещенное
