# TSP Branch-and-Bound Search Tree

## Description

The Travelling Salesperson Problem (TSP) requires finding a minimum-cost tour in which every city is visited exactly once and the tour returns to the starting city.

This project demonstrates the Branch-and-Bound method for TSP using four cities: A, B, C, and D. The method constructs a search tree of possible tours and uses lower bounds to avoid exploring branches that cannot improve the current best solution.

For the given cost matrix, an optimal tour is:

**A → B → D → C → A**

The minimum total cost is **80**.

## Problem Statement

Draw a search tree showing bounding and pruning for TSP with 4 cities using the Branch-and-Bound technique.

## Input

The cost matrix used is:

| City | A | B | C | D |
|---|---:|---:|---:|---:|
| A | 0 | 10 | 15 | 20 |
| B | 10 | 0 | 35 | 25 |
| C | 15 | 35 | 0 | 30 |
| D | 20 | 25 | 30 | 0 |

## Algorithm

1. Start from city A.
2. Calculate the initial lower bound.
3. Mark A as visited.
4. Generate branches by selecting an unvisited city.
5. Calculate the path cost for the selected branch.
6. Calculate its lower bound.
7. Add the path cost and bound to estimate the minimum possible completion cost.
8. If the estimated cost is smaller than the current best cost, explore the branch.
9. Otherwise, prune the branch.
10. When all cities are visited, add the cost of returning to A.
11. Update the best tour if the new tour has a smaller cost.
12. Continue until all useful branches have been considered.
13. Return the optimal tour and minimum cost.

## Pseudocode

```text
TSP_Branch_and_Bound()

    Calculate initial lower bound

    Start from city A
    Mark A as visited

    Explore every unvisited city

        Calculate path cost
        Calculate lower bound

        IF lower_bound + path_cost < current_best_cost
            Expand the branch
        ELSE
            Prune the branch

    IF all cities are visited
        Add cost of returning to A
        Update best tour if required

    Return optimal tour and minimum cost
```

## Branch-and-Bound Concept

### Branching

Branching creates different possible choices for the next city.

For example, after starting from A:

```text
A → B
A → C
A → D
```

Each branch represents a possible partial tour.

### Bounding

A lower bound estimates the minimum possible cost of completing a partial tour.

The bound helps determine whether a branch is worth exploring.

### Pruning

If the estimated cost of a branch is not better than the current best solution, that branch is discarded.

This reduces unnecessary exploration of the search tree.

## Optimal Tour

One optimal tour for the given matrix is:

```text
A → B → D → C → A
```

Cost:

```text
A → B = 10
B → D = 25
D → C = 30
C → A = 15
----------------
Total   = 80
```

Therefore:

**Minimum Cost = 80**

## Visualization

The file `Visualization.png` presents the search-tree concept for the four-city TSP.

It shows:

- Starting city
- Possible branches
- Partial tour costs
- Bound/estimated values
- Explored branches
- Pruned branches
- Optimal tour
- Minimum cost

## Prompt Used

The visualization prompt is stored in:

`Prompt.txt`

The prompt describes the four-city cost matrix and asks for a search tree showing branching, bounds, pruning, and the optimal tour.

## Complexity

TSP has factorial growth in the number of possible tours. The basic brute-force approach has approximately:

```text
O(n!)
```

Branch-and-Bound can reduce the practical search space by pruning unpromising branches, although the worst-case complexity remains exponential/factorial.

## Learning Outcomes

- Understood the Travelling Salesperson Problem.
- Learned the Branch-and-Bound technique.
- Understood branching and bounding.
- Learned how pruning reduces unnecessary search.
- Understood lower-bound estimation.
- Visualized a TSP search tree.
- Practiced algorithm documentation and visualization.
- Practiced organizing a project using GitHub.

## Files

```text
Project14_TSP_BranchAndBound.py
Prompt.txt
Visualization.png
README.md
```

## Conclusion

This project demonstrates how Branch-and-Bound solves the Travelling Salesperson Problem by exploring possible tours and eliminating branches that cannot produce a better solution.

For the given four-city example, the optimal tour is:

**A → B → D → C → A**

with a minimum cost of:

**80**
