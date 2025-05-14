import java.util.*;

public class baekjoon_5597 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int[] list = new int[31];

        for (int i=0; i<31; i++){
            list[i] = 0;
        }

        for (int i=0; i<28; i++){
            int a = scanner.nextInt();
            list[a] = 1;
        }

        for (int i=1; i<31; i++){
            if(list[i] == 0){
                System.out.println(i);
            }
        }
        scanner.close();
    }
}

// 배열 생성 int[] list = new int[31];