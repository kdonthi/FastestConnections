# FastestConnections

## Introduction
This project finds the fastest connections between two points on a directed K6 (directed complete graph with 6 vertices); I used a dynamic programming algorithm to find the solution in O(1).

## Input Details
I thought of each vertex as a letter from A to F. The input file should be an adjacency matrix with the weight of connection A -> B is in row A and column B. Each value is seperated by a space and each row is seperated by a newline.

After the adjacency matrix, include the starting vertex after `"Source"` and the ending vertex after `"Target"`.

Samples of inputs can be find in `input.txt` and `input2.txt`.
