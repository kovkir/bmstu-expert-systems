from items import Rule, Node

NODE_1 = Node(1)
NODE_2 = Node(2)
NODE_3 = Node(3)
NODE_4 = Node(4)
NODE_5 = Node(5)
NODE_6 = Node(6)
NODE_7 = Node(7)
NODE_8 = Node(8)
NODE_9 = Node(9)
NODE_10 = Node(10)
NODE_11 = Node(11)
NODE_12 = Node(12)
NODE_13 = Node(13)
NODE_14 = Node(14)
NODE_15 = Node(15)
NODE_16 = Node(16)
NODE_17 = Node(17)
NODE_18 = Node(18)
NODE_19 = Node(19)
NODE_20 = Node(20)
NODE_21 = Node(21)
NODE_22 = Node(22)

RULES = [
    Rule(101, NODE_5,  [NODE_1,  NODE_2]),
    Rule(102, NODE_11, [NODE_3,  NODE_4, NODE_5]),
    Rule(103, NODE_13, [NODE_5,  NODE_6, NODE_19]),
    Rule(104, NODE_13, [NODE_2,  NODE_7, NODE_8]),
    Rule(105, NODE_15, [NODE_7,  NODE_8, NODE_9]),
    Rule(106, NODE_16, [NODE_10, NODE_11]),
    Rule(107, NODE_17, [NODE_11, NODE_12, NODE_13]),
    Rule(108, NODE_17, [NODE_13, NODE_14, NODE_15]),
    Rule(109, NODE_18, [NODE_14, NODE_15]),
    Rule(110, NODE_19, [NODE_20, NODE_21]),
    Rule(111, NODE_19, [NODE_21, NODE_22]),
    Rule(112, NODE_8,  [NODE_22]),
]
