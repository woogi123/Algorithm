import java.util.Scanner;

public class baekjoon_2480 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int z = scanner.nextInt();

        if (x == y && y == z) {
            System.out.printf("%d", 10000 + 1000 * x);
        } else if (x == y || x == z) {
            System.out.printf("%d", 1000 + 100 * x);
        } else if (y == z) {
            System.out.printf("%d", 1000 + 100 * y);
        } else {
            int max = Math.max(x, Math.max(y, z));
            System.out.printf("%d", 100 * max);
        }
        // Math 클래스 사용

        scanner.close();
    }
}
