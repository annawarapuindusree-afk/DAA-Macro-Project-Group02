Algorithm JobSequencing(Jobs)

Input:
    A set of n jobs.
    Each job has:
        job_id
        deadline
        profit

Output:
    Schedule of jobs with maximum profit.

1. Sort all jobs in decreasing order of profit.

2. Find the maximum deadline.

3. Create an array slot[] of size maxDeadline.
   Initially mark all slots as empty.

4. For each job in sorted order:
       For j = job.deadline down to 1:
           
           If slot[j] is empty:
               slot[j] = job
               Add job.profit to totalProfit
               Break

5. Return the scheduled jobs and totalProfit.