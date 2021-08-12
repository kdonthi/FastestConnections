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

def parse_input(fileName):
    nodes = "ABCDEF"
    connectionsDict = {}
    with open(fileName, "r") as file:
        fileList = list(file)
        for line in fileList[0:6]:
            currNode = None
            nodeIndex = 0
            for index, element in enumerate(line.split(" ")):
                if index == 0:
                    connectionsDict[element] = {}
                    currNode = element
                else:
                    connectionsDict[currNode][nodes[nodeIndex]] = int(element)
                    nodeIndex += 1
        source = fileList[7].split(" ")[1]
        dest = fileList[8].split(" ")[1]

        return connectionsDict, source, dest


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    dictionary, src, dest = parse_input("input.txt")
    for node in dictionary:
        print(node, dictionary[node])
    print(src)
    print(dest)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
