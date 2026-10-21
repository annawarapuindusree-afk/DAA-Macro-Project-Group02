import java.util.*;

class Job {
    char id;
    int deadline, profit;

    Job(char id, int deadline, int profit) {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }
}

public class JobSequencing {

    public static void main(String[] args) {

        Job[] jobs = {
            new Job('J1', 2, 100),
            new Job('J2', 1, 19),
            new Job('J3', 2, 27),
            new Job('J4', 1, 25),
            new Job('J5', 3, 15)
        };

        Arrays.sort(jobs, (a, b) -> b.profit - a.profit);

        int maxDeadline = 0;

        for (Job job : jobs)
            maxDeadline = Math.max(maxDeadline, job.deadline);

        char[] slot = new char[maxDeadline + 1];
        int totalProfit = 0;

        for (Job job : jobs) {

            for (int j = job.deadline; j >= 1; j--) {

                if (slot[j] == '\0') {
                    slot[j] = job.id;
                    totalProfit += job.profit;
                    break;
                }
            }
        }

        System.out.println("Scheduled Jobs:");

        for (int i = 1; i <= maxDeadline; i++)
            System.out.print(slot[i] + " ");

        System.out.println("\nMaximum Profit = " + totalProfit);
    }
}