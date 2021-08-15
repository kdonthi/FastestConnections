"""
Exercise:

The goal is to find the fastest path in a graph.

You have a graph of 6 nodes. Each node is connected to the other. Connection from Node1 to Node2 is not the same in the cost as connection from Node2 to Node1. This means there are 6*5 = 30 connections.

Given the graph connection cost (you can set it as you want). you should find the fastest route between node1 and node2.

Your program should accept a file that contains the graph connections cost, the name of source and target nodes.

The program should return the fastest route, and the cost of each leg.

For example: SourceNode -- (5) --> Node1 -- (7) -->  Node2 -- (3) --> TargetNode

You will be checked on:

1. correct result

2. code optimization (how much time it took to find the fastest route)

3. clear code (writing standards)
"""

import sys
import os


nodes = "ABCDEF"
connectionCosts = {}
def parse_input(fileName):
    connectionsDict = {}
    with open(fileName, "r") as inputFile:
        fileList = list(inputFile)
        for line in fileList[0:6]:
            currNode = None
            nodeIndex = 0
            for index, element in enumerate(line.split(" ")):
                if index == 0:
                    connectionsDict[element] = {}
                    currNode = element
                else:
                    dest = nodes[nodeIndex]
                    connectionsDict[currNode][dest] = [False, int(element), [currNode, dest]] #Has minimum for this path been found, cost, path
                    nodeIndex += 1
        source = fileList[7].split(" ")[1].strip()
        dest = fileList[8].split(" ")[1].strip()
        return connectionsDict, source, dest

def solve_tree():
    args = sys.argv
    if len(args) != 2:
        print(args)
        print(len(args))
        raise Exception("Make sure there is only one argument, and that it is the input filename (e.g. \"python3 main.py input.txt\")")
    filename = args[1]
    if not os.path.exists(filename):
        raise Exception("Not a valid filepath.")
    if filename[-4:] != ".txt":
        raise Exception("Not a .txt file.")

    global connectionCosts
    connectionCosts, src, dest = parse_input(filename)
    cost, path = findLowestCostPath(src, dest, [src])
    print("Cost: ", end="")
    print(cost)
    for i in range(len(path[:-1])):
        if i != 0:
            print(" ", end="")
        print(path[i], end="")
        print(" -- (", end="")
        print(connectionCosts[path[i]][path[i + 1]][1], end="")
        print(") -->", end="")
    print(" " + path[-1])

def findLowestCostPath(src: str, dest: str, visited: list[str]): #return path, cost, include src in visited
    nodesToVisitNext = []
    for node in nodes:
        if node not in visited and node != src:
            if node == dest:
                nodesToVisitNext.append((connectionCosts[src][node][1], [src, dest]))
            else:
                #memoization
                if not connectionCosts[node][dest][0]:
                    set_connection_cost(node, dest, visited)
                nodesToVisitNext.append((connectionCosts[src][node][1] + connectionCosts[node][dest][1], [src] + connectionCosts[node][dest][2]))
    nodesToVisitNext.sort(key=lambda x: x[0]) #sorting by connnection costs
    return nodesToVisitNext[0]


def set_connection_cost(node, dest, visited):
    lowestCost, path = findLowestCostPath(node, dest, visited + [node])
    connectionCosts[node][dest][1] = lowestCost
    connectionCosts[node][dest][2] = path
    connectionCosts[node][dest][0] = True


if __name__ == "__main__":
    solve_tree()
