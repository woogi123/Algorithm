import java.util.Scanner;

public class baekjoon_10951 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNext()){
            int a = scanner.nextInt();
            
            int b = scanner.nextInt();
            System.out.println(a+b);
        }

        scanner.close();
    }
}
