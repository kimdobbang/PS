import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();
        String T = sc.next();
        int hammingDistance = 0;
        for(int i=0; i<N; i++) {
            if (S.charAt(i) != T.charAt(i)) {
                hammingDistance++;
            }
        }
        System.out.println(hammingDistance);
    }
}
       