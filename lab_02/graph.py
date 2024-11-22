import graphviz

from items import Rule, Node


def buildGraph(
    rules: list[Rule],
    goal_node: Node, 
    in_node_arr: list[Node],
    graph_name: str,
    close_node_lst: list[Node] | None = None,
    close_rule_lst: list[Rule] | None = None,
) -> None:
    dot = graphviz.Digraph(
        comment=f'lab_02_{graph_name}'
    )
    nodes = []
    for rule in rules:
        nodes.append(str(rule.out_node.number))
        if close_rule_lst and rule in close_rule_lst:
            dot.node(
                name=str(rule.number),
                shape="rectangle",
                color="purple4", 
                style="filled", 
                fillcolor="plum",
            )
        else:
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
        elif close_node_lst and node in \
            [str(close_node.number) for close_node in close_node_lst]:
            dot.node(
                name=node, 
                color="purple4", 
                style="filled", 
                fillcolor="plum",
            )
        else:
            dot.node(node)

    dot.render(f'./docs/{graph_name}.gv').replace('\\', '/')
