import java.util.*;

public class Project11_SumOfSubsets {

    static int[] a;
    static int target;
    static boolean found = false;

    static void solve(int i, int sum, ArrayList<Integer> list) {

        if (i == a.length) {
            if (sum == target) {
                System.out.println(list);
                found = true;
            }
            return;
        }

        list.add(a[i]);
        solve(i + 1, sum + a[i], list);

        list.remove(list.size() - 1);

        solve(i + 1, sum, list);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        a = new int[n];

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        System.out.print("Enter target sum: ");
        target = sc.nextInt();

        System.out.println("Subsets with sum " + target + ":");

        solve(0, 0, new ArrayList<>());

        if (!found) {
            System.out.println("No subset found");
        }

        sc.close();
    }
}