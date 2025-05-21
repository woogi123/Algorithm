import java.util.*;

public class baekjoon_1018 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        scanner.nextLine();
        
        char[][] board = new char[N][M];
        for (int i = 0; i < N; i++) {
            board[i] = scanner.nextLine().toCharArray();
        }

        int min = Integer.MAX_VALUE;


        for (int i = 0; i <= N - 8; i++) {
            for (int j = 0; j <= M - 8; j++) {
                int count1 = 0;
                int count2 = 0;
                
                for (int x = 0; x < 8; x++) {
                    for (int y = 0; y < 8; y++) {
                        char expected1 = ((x + y) % 2 == 0) ? 'W' : 'B';
                        char expected2 = ((x + y) % 2 == 0) ? 'B' : 'W';

                        if (board[i + x][j + y] != expected1) count1++;
                        if (board[i + x][j + y] != expected2) count2++;
                    }
                }

                int minCount = Math.min(count1, count2);
                min = Math.min(min, minCount);
            }
        }

        System.out.println(min);
        scanner.close();
    }
}
