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

NODE_11 = Node(11)
NODE_12 = Node(12)
NODE_13 = Node(13)
NODE_14 = Node(14)
NODE_15 = Node(15)
NODE_17 = Node(17)
NODE_18 = Node(18)
NODE_19 = Node(19)
NODE_20 = Node(20)
NODE_21 = Node(21)
NODE_22 = Node(22)
NODE_23 = Node(23)
NODE_24 = Node(24)

NODE_31 = Node(31)
NODE_33 = Node(33)

RULES = [
    Rule(101, NODE_3,  [NODE_1,  NODE_2]),
    Rule(102, NODE_7,  [NODE_3,  NODE_2, NODE_4]),
    Rule(103, NODE_4,  [NODE_5,  NODE_6]),
    Rule(104, NODE_3,  [NODE_8,  NODE_31]),
    Rule(105, NODE_14, [NODE_7,  NODE_9]),
    Rule(106, NODE_9,  [NODE_4,  NODE_18, NODE_11]),
    Rule(107, NODE_11, [NODE_12, NODE_13]),
    Rule(108, NODE_33, [NODE_21, NODE_15]),
    Rule(110, NODE_14, [NODE_9,  NODE_21]),
    Rule(111, NODE_9,  [NODE_11, NODE_17]),
    Rule(112, NODE_21, [NODE_17, NODE_19]),
    Rule(113, NODE_17, [NODE_12, NODE_20]),
    Rule(114, NODE_12, [NODE_22, NODE_23]),
    Rule(115, NODE_21, [NODE_19, NODE_24]),
    Rule(116, NODE_19, [NODE_13, NODE_20, NODE_24])
]
