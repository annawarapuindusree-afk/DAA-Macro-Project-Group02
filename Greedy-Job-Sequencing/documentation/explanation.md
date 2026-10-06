# Greedy Job Sequencing with Deadlines and Profits

## 1. Problem Statement

Given a set of jobs where each job has a deadline
and profit, schedule the jobs to maximize total profit.

Each job requires one unit of time.

## 2. Greedy Strategy

Jobs are sorted in decreasing order of profit.

For each job, we try to place it in the latest
available time slot before its deadline.

## 3. Example

J1 = deadline 2, profit 100
J2 = deadline 1, profit 19
J3 = deadline 2, profit 27
J4 = deadline 1, profit 25
J5 = deadline 3, profit 15

## 4. Final Schedule

J3 → J1 → J5

## 5. Maximum Profit

142

## 6. Time Complexity

O(n log n + n*d)

## 7. Space Complexity

O(d)

## 8. Visualization

The flowchart illustrates how jobs are selected,
checked against deadlines and assigned to available slots.