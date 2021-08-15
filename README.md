# FastestConnections

## Introduction
This project finds the fastest connections between two points on a directed K6 (directed complete graph with 6 vertices); I used a dynamic programming algorithm to find the solution in O(V^2), where V is the number of vertices.

## Input Details
I thought of each vertex as a letter from A to F. The input file should be an adjacency matrix with the weight of connection A -> B is in row A and column B. Each value is seperated by a space and each row is seperated by a newline.

After the adjacency matrix, include the starting vertex after `"Source: "` and the ending vertex after `"Target: "`. (Note: make sure that `Source:` and `Target:` have a space after them and before the number.)

Samples of inputs can be find in `input.txt` and `input2.txt`.

## Running the program/Output
The program can be run using `python3 main.py [INPUT_FILE_NAME]` and should produce an output like this: `B -- (1) --> C -- (1) --> D -- (2) --> E`, where nodes and costs in the lowest cost path are shown.

The time taken to find the result will also be shown after.

