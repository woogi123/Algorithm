import java.util.Scanner;

public class baekjoon_2480 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int z = scanner.nextInt();

        if (x == y){
            if (y == z){
                System.out.printf("%d", 10000 + 1000 * x);
            }else{
                System.out.printf("%d", 1000 + 100*x);
            }
        }else{
            if (y == z){
                System.out.printf("%d", 1000 + 100*y);
            }else{
                if (x > y){
                    if(x > z){
                        System.out.printf("%d", 100*x);
                    }else{
                        System.out.printf("%d", 100*z);
                    }
                }else{
                    if(y > z){
                        System.out.printf("%d", 100*y);
                    }else{
                        System.out.printf("%d", 100*z);
                    }
                }
                }
            }

        scanner.close();
    }
}
