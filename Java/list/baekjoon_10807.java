import java.util.*;

public class baekjoon_10807 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        
        List<Integer> list = new ArrayList<>();
        
        for(int i=0; i<N; i++){
            list.add(scanner.nextInt());
        }
        int v = scanner.nextInt();
        int count = Collections.frequency(list, v);
        System.out.println(count);


        scanner.close();
    }    
}

 // Collectoin.frequency: find v in list
 // List<Integer> list = new ArrayList<>(); -> 연속되게 해야만 함. ([1][2][3][][4]) X
 // List<String> list = new ArrayList<>();
