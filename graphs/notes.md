# GRAPH THEORY
Source: freeCodeCamp.org
[Youtube video-course](https://www.youtube.com/watch?v=09_LlHjoEiY&ab_channel=freeCodeCamp.org)

**Graph theory** is the mathematical theory of the properties and applications of graphs (networks).

It can be applied to almost every problem. Examples: social network friends.

## 1. Types of graphs
- Undirected graph
    - Edges have no orientation. The edge (u, v) is identical to the edge (v, u).
- Directed graph (Digraph)
    - Edges have orientations. The edge (u, v) is the edge from node u to node v.
- Weighted graphs
    - Edges contain a certain weight to represent an arbitrary value such as cost, distance...
- Trees
    - Undirected graph with no cycles.
- Rooted trees
- Directed acyclic graphs (DAGs)
    - Schedulers, class requirements, ...
- Bipartite graphs
- Complete graphs.
    - Unique edge between every pari of nodes.
    - Worst-case possible graph.

## 2. Representing graphs
- **Adjacency matrix**: is a very simple way to represent a graph. The idea is that the cell m[i][j] represents the edge weight of going from node i to node j.
    - Pros: 
        - space efficient for representing dense graphs.
        - edge weight lookup is O(1).
        - simplest graph representation.
    - Cons:
        - requires O(v2) space.
        - iterating over all edges takes O(v2) time.

- **Adjacency list**: map from nodes to lists of edges. Only need to track the node we are going to and the weight; we don't need to keep track of where we came from, because that's implicitly known.
    - Pros:
        - space efficient for representing sparse graphs.
        - iterating over all edges is efficient.
    - Cons:
        - less space efficient for denser graphs.
        - edge weight lookup is O(E).
        - slightly more complex graph representation.

- **Edge list**: unordered list of edges. Rarely used because of its lack of structure.
    - Pros:
        - space efficient for representing sparse graphs.
        - iterating over all edges is efficient.
        - very simple structure.
    - Cons:
        - less space efficient for denser graphs.
        - edge weight lookup is O(E).

## 3. Common graph theory problems
### Shortest path problem
Given a weighted graph, find the shortest path of edges from node A to node B.
- Algorithms: BFS (unweighted graph), Dijkstra's, Bellman-Ford, Floyd-Warshall, A*, etc.

### Connectivity
Does there exist a path between node A and node B?
- Typical solution: use union find data structure or any search algorithm (DFS)

### Negative cycles
Does my weighted digraph have any negative cycles? If so, where?

In the context of finding the shortest path, a negative cycle is a trap that you can't never scape from.

However, sometimes negative cycles might be beneficial. Suppose we are trading currencies, if you find a negative cycle you could do arbitrage to make money.

- Algorithms: Bellman-Ford and Floyd-Warshall.

### Strongly connected components (SCCs)
They can be thought of as self-contained cycles within a directed graph where every vertex in a given cycle can reach every other vertext in the same cycle.

- Algorithms: Tarjan's and Kosaraju's algorithm.

### Traveling salesman problem (TSP)
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

The TSP problem is NP-Hard, meaning it's a very computationally challenging problem. This is unfortunate because the TSP has several very important applications.

- Algorithms: Held-Karp, branch and bound and many approximation algorithms.

### Bridges
A *bridge / cut edge* is any edge in a graph whose removal increases the number of connected components.

Bridges are important in graph theory because they often hint at weak points, bottlenecks or vulnerabilities in a graph.

### Articulation points
An *articulation point / cut vertex* is any node in a graph whose removal increases the number of connected components.

Articulation points are important in graph theory because they often hint at weak points, bottlenecks or vulnerabilities in a graph.

### Minimum spanning tree (MST)
A *minimum spanning tree* is a subset of the edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

- Algorithms: Kruskal's, Prim's & Boruvka's algorithm.
- Applications: designing a least cost network, circuit design, transportation networks, etc.

### Network flow: max flow.
With an infinite input source how much "flow" can we push through the network?

Suppose the edges are roads with cars, pipes with water or hallways packed with people. Flow represents the volume of water allowed to flow through the pipes, the number of cars the roads can sustain in traffic and the maximum amount of people that can navigate through the hallways.

- Algorithms: Ford-Fulkerson, Edmonds-Karp & Dinic's algorithm.

## 4. DEPTH FIRST SEARCH (DSF)
- It's the most fundamental search algorithm used to explore nodes and edges of a graph.
- O(V+E) time complexity.
- Often used as a building block in other algorithm.

By itself the DFS isn't all that useful, but when augmented to perform other takss such as count connected components, determine connectivity, or find bridges/articulation points, then DFS really shines.

DFS plunges depth first into a graph without regard for which edge it takes next until it cannot go any further at which point it backtracks and continues.

Applications: topological sorting, scheduling problems, cycle detection in graphs, solving puzzles with only one solution (sudoku), maping routes, etc.

### Connected Components
Sometimes a graph is split into multiple components. It's useful to be able to identify and count these components.

We can use a DFS to identify components.
1. Make sure all the nodes are labeled from [0, n), where *n* is the number of nodes.
2. Start a DFS at every node (except if it's already been visited) and mark all reachable nodes as being part of the same component.

### What else can DFS do?
- Compute a graph's minimum spanning tree.
- Detect and find cycles in a graph.
- Check if a graph is bipartite.
- Find strongly connected components.
- Topologically sort the nodes of a graph.
- Find bridges and articulation points.
- Find augmenting paths in a flow network.
- Generate mazes.

## 5. BREADTH FIRST SEARCH (BFS)
The BFS is another fundamental search algorithm used to explore nodes and edges of a graph. It runs with a time complexity of O(V+E) and is often used as a building block in other algorithms.

The BFS algorithm is particularly useful for one thing: finding the shortest path on unweighted graphs.

A BFS starts at some arbitrary node of a graph and explores the neighbour nodes first, before moving to the next level neighbours.

It explores the graph in a layer phasion. It does that by maintaining a queue of which node it should visit next.

### BFS shortest path on a grid
Motivation: many problems in graph theory can be represented using a grid. Grids are a form of implicit graph because we can determine a node's neighbours based on our location within the grid.

A common approach to solving graph theory problems on grids is to first convert the grid to a familiar format such as an adjacency list/matrix.

Convert an empty grid into an adjacency list:
1. Label the cells in the grid with numbers [0, n), where `n = n_rows x n_columns`.
2. Form an adjancency matrix n * n.
3. Run whatever specialized graph algorithm to solve our problem (shortest path, connected components, ...).

However, transformations between graph representations can usually be avoided due to the structure of a grid. If we are at a `red ball` in the middle we can move left, right, up and down to reach adjacent cells. Mathematically, if the `red ball` is at the row-column coordinate (r, c) we can add the row vectors `[-1, 0]`, `[1, 0]`, `[0, 1]`, and `[0, -1]` to reach adjacent cells. If the problem allows moving diagonally then you can also include the row vectors: `[-1, -1]`, `[-1, 1]`, `[1, 1]`, `[1, -1]`
