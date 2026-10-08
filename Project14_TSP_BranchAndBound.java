import java.util.*;

public class TSPBranchBound {

    static int N = 4;

    // Cost matrix for cities A, B, C and D
    static int[][] cost = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    static int finalCost = Integer.MAX_VALUE;
    static ArrayList<Integer> finalPath = new ArrayList<>();

    static boolean[] visited = new boolean[N];

    // Find the minimum edge from city i
    static int firstMin(int i) {
        int minimum = Integer.MAX_VALUE;

        for (int k = 0; k < N; k++) {
            if (i != k && cost[i][k] < minimum) {
                minimum = cost[i][k];
            }
        }

        return minimum;
    }

    // Find the second minimum edge from city i
    static int secondMin(int i) {
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        for (int j = 0; j < N; j++) {

            if (i == j) {
                continue;
            }

            if (cost[i][j] <= first) {
                second = first;
                first = cost[i][j];
            }
            else if (cost[i][j] < second) {
                second = cost[i][j];
            }
        }

        return second;
    }

    // TSP Branch and Bound
    static void tspBranchBound(
            double bound,
            int weight,
            int level,
            ArrayList<Integer> path) {

        // All cities are visited
        if (level == N) {

            int currentCost =
                    weight + cost[path.get(level - 1)][path.get(0)];

            if (currentCost < finalCost) {
                finalCost = currentCost;

                finalPath = new ArrayList<>(path);
                finalPath.add(path.get(0));
            }

            return;
        }

        // Try every unvisited city
        for (int city = 0; city < N; city++) {

            if (!visited[city]) {

                int previousCity = path.get(level - 1);

                double newBound = bound;

                if (level == 1) {

                    newBound -=
                            (firstMin(previousCity)
                            + firstMin(city)) / 2.0;

                } else {

                    newBound -=
                            (secondMin(previousCity)
                            + firstMin(city)) / 2.0;
                }

                int newWeight =
                        weight + cost[previousCity][city];

                // Branch and Bound condition
                if (newBound + newWeight < finalCost) {

                    path.add(city);
                    visited[city] = true;

                    tspBranchBound(
                            newBound,
                            newWeight,
                            level + 1,
                            path
                    );

                    // Backtracking
                    visited[city] = false;
                    path.remove(path.size() - 1);
                }
            }
        }
    }

    static void solveTSP() {

        double bound = 0;

        // Calculate initial lower bound
        for (int i = 0; i < N; i++) {
            bound += firstMin(i) + secondMin(i);
        }

        bound = Math.ceil(bound / 2.0);

        // Start from city A (0)
        visited[0] = true;

        ArrayList<Integer> path = new ArrayList<>();
        path.add(0);

        tspBranchBound(
                bound,
                0,
                1,
                path
        );

        // City names
        char[] cityNames = {'A', 'B', 'C', 'D'};

        System.out.println("Optimal Tour:");

        for (int i = 0; i < finalPath.size(); i++) {

            System.out.print(
                    cityNames[finalPath.get(i)]
            );

            if (i < finalPath.size() - 1) {
                System.out.print(" -> ");
            }
        }

        System.out.println();
        System.out.println("\nMinimum Cost: " + finalCost);
    }

    public static void main(String[] args) {
        solveTSP();
    }
}