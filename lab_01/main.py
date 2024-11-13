import graphviz
from copy import deepcopy

from graphBFS import GraphBFS
from graphDFS import GraphDFS
from items import Edge
from data import *


def buildGraph(edges: list[Edge]) -> None:
    dot = graphviz.Digraph(
        comment='Граф для поиска в глубину и ширину'
    )
    nodes = []
    for edge in edges:
        nodes.append(str(edge.startNode.number))
        nodes.append(str(edge.endNode.number))
        dot.edge(
            str(edge.startNode.number), 
            str(edge.endNode.number), 
            constraint='true',
        )
    for node in list(dict.fromkeys(nodes)):
        dot.node(node)

    dot.render('./docs/graph.gv').replace('\\', '/')


def searchInDepth(edgeList: list[Edge], start: int, goal: int) -> None:
    print("\n\tПОИСК В ГЛУБИНУ\n")
    res = GraphDFS(edgeList).find(
        start=start, 
        goal=goal,
    )
    GraphDFS.showResult(res)


def searchInWidth(edgeList: list[Edge], start: int, goal: int) -> None:
    print("\n\tПОИСК В ШИРИНУ\n")
    res = GraphBFS(edgeList).find(
        start=start, 
        goal=goal,
    )
    GraphBFS.showResult(res)


def main(edgeList: list[Edge], start: int, goal: int) -> None:
    buildGraph(edgeList)
    searchInDepth(
        edgeList=deepcopy(edgeList),
        start=start,
        goal=goal,
    )
    searchInWidth(
        edgeList=deepcopy(edgeList),
        start=start,
        goal=goal,
    )


if __name__ == "__main__":
    main(
        edgeList=EDGE_LIST,
        start=0,
        goal=6,
    )
