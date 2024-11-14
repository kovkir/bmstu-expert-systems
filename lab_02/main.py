from data import *
from items import Node
from search import Search
from graph import buildGraph


def main(goal_node: Node, in_node_arr: list[Node]):
    buildGraph(
        rules=RULES,
        goal_node=goal_node,
        in_node_arr=in_node_arr,
        graph_name="initial_graph",
    )
    search = Search(RULES)
    search.run(
        goal_node=goal_node,
        in_node_arr=in_node_arr.copy(),
    )
    buildGraph(
        rules=RULES,
        goal_node=goal_node,
        in_node_arr=in_node_arr,
        close_node_lst=search.close_node_lst,
        close_rule_lst=search.close_rule_lst,
        graph_name="final_graph",
    )


if __name__ == "__main__":
    main(
        goal_node=NODE_17,
        in_node_arr=[
            NODE_1, NODE_2, NODE_3, NODE_4, 
            NODE_6, NODE_12, NODE_21, NODE_22,
        ],
    )
