import graphviz

from data import (
    RULES, 
    NODE_14, NODE_5, NODE_6, NODE_2, NODE_1,
    NODE_18, NODE_22, NODE_23, NODE_7, NODE_13
)
from items import Rule, Node
from search import Search


def buildGraph(
    rules: list[Rule],
    goal_node: Node, 
    in_node_arr: list[Node],
) -> None:
    dot = graphviz.Digraph(
        comment='lab_02'
    )
    nodes = []
    for rule in rules:
        nodes.append(str(rule.out_node.number))
        dot.node(
            name=str(rule.number),
            shape="rectangle",
        )
        dot.edge(
            tail_name=str(rule.out_node.number), 
            head_name=str(rule.number),
            constraint='true',
            arrowhead="none",
        )
        for node in rule.node_arr:
            nodes.append(str(node.number))
            dot.edge(
                tail_name=str(rule.number),
                head_name=str(node.number),
                constraint='true',
                arrowhead="none",
            )
    for node in list(dict.fromkeys(nodes)):
        if node == str(goal_node.number):
            dot.node(
                name=node, 
                color="darkgreen", 
                style="filled", 
                fillcolor="lightgreen",
            )
        elif node in [str(in_node.number) for in_node in in_node_arr]:
            dot.node(
                name=node, 
                color="darkblue", 
                style="filled", 
                fillcolor="lightblue",
            )
        else:
            dot.node(node)

    dot.render('./docs/graph.gv').replace('\\', '/')


def main(goal_node: Node, in_node_arr: list[Node]):
    buildGraph(
        rules=RULES,
        goal_node=goal_node,
        in_node_arr=in_node_arr,
    )
    Search(RULES).run(
        goal_node=goal_node, 
        in_node_arr=in_node_arr,
    )


if __name__ == "__main__":
    main(
        goal_node=NODE_14,
        in_node_arr=[
            NODE_5, NODE_6, NODE_2, 
            NODE_1, NODE_18, NODE_22, 
            NODE_23, NODE_7, NODE_13,
        ],
    )
