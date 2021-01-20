# DYNAMIC PROGRAMMING - MEMOIZATION
1. Make it work.
    - visualize the problem as a tree: large problem broken down into smaller instances of the same problem. 
        - Each node is a sub-problem. 
        - Each edge shrinks the problem.
        - Each leaf is a base-case solution.
    - implement the tree using recursion.
    - test it.

2. Make it efficient.
    - add a memo object.
    - add a base case to return memo values.
    - store return values into the memo.

**Exercices**
- can_sum: can you do it? yes/no.
    - decision problem.
- how_sum: how will you do it? one solution.
    - combinatoric problem.
- best_sum: what's the best way to do it? best solution. 
    - optimization problem.