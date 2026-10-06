# Sum of Subsets using Backtracking

## Description

The Sum of Subsets problem is a classic backtracking problem in which
we find all subsets of a given set whose sum is equal to a specified
target value.

The program accepts a set of integers and a target sum as input.
For every element, the algorithm explores two possibilities:

1. Include the element in the current subset.
2. Exclude the element from the current subset.

Backtracking is used to explore all possible subsets and identify
the subsets whose sum is equal to the target.

For visualization, the example specified in the project is:

Set = {5, 10, 12}

Target Sum = 15

The successful subset is:

{5, 10}

because:

5 + 10 = 15


## Algorithm

1. Start with an empty subset and current sum equal to 0.
2. Consider the elements of the input set one by one.
3. Include the current element in the subset and recursively process
   the next element.
4. Backtrack by removing the current element.
5. Exclude the current element and recursively process the next element.
6. When all elements have been considered, check whether the current
   sum is equal to the target.
7. If the sum equals the target, display the current subset.
8. Continue the process to find all possible subsets.


## Pseudocode

SUM_OF_SUBSETS(index, currentSum, subset)

    if index == number of elements
        if currentSum == target
            print subset
        return

    add array[index] to subset

    SUM_OF_SUBSETS(index + 1,
                   currentSum + array[index],
                   subset)

    remove array[index] from subset

    SUM_OF_SUBSETS(index + 1,
                   currentSum,
                   subset)


## Prompt Used

Create a state-space tree visualization for the Sum of Subsets
problem using the Backtracking algorithm.

The visualization should work conceptually for any given set of
integers and a target sum.

At each level of the state-space tree, consider one element of the
set and show two choices:

1. Include the current element in the subset.
2. Exclude the current element from the subset.

Each node should display:
- The elements currently selected in the subset.
- The current sum.
- The decision made (Include or Exclude).

Continue exploring recursively until all elements have been considered.

Clearly identify:
- Successful branches where the subset sum equals the target.
- Unsuccessful branches where the target is not achieved.
- Backtracking from one branch to explore another possible subset.

Use the following example to demonstrate the visualization:

Set = {5, 10, 12}
Target Sum = 15

Highlight {5, 10} as a successful subset because:

5 + 10 = 15

Generate a clear and structured state-space tree suitable for a
Design and Analysis of Algorithms project.


## Output

### Example Input

Enter number of elements: 3

Enter the elements:
5 10 12

Enter target sum: 15

### Example Output

Subsets with sum 15:

[5, 10]


## Visualization

The generated state-space tree is available in:

Visualization.png

The tree represents the recursive exploration of subsets.

Each level represents one element of the input set and each node
has two possible decisions:

- Include the current element
- Exclude the current element

For the example {5, 10, 12}, the branch containing {5, 10}
reaches the target sum 15 and is therefore marked as successful.

Other branches represent subsets that do not produce the required
target sum.

The visualization demonstrates how backtracking explores different
choices and returns to previous states to examine other possibilities.


## How to Compile and Run

Compile:

javac Project11_SumOfSubsets.java

Run:

java Project11_SumOfSubsets


## Files

Project11_SumOfSubsets.java - Java implementation of the algorithm

Prompt.txt - Prompt used for generating the visualization

Visualization.png - State-space tree visualization

README.md - Project documentation


## Learning Outcome

- Understood the Sum of Subsets problem.
- Learned the backtracking technique.
- Understood include and exclude decisions in backtracking.
- Learned how a state-space tree represents recursive exploration.
- Learned how to find subsets that satisfy a target sum.
- Learned prompt-based algorithm visualization.
- Practiced GitHub project documentation.