// 末尾の文字 (Last Letter)

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();

        if (S.charAt(N - 1) == 'G') {
            for (int i = 0; i < N - 1; i++) {
                System.out.print(S.charAt(i));
            }
        } else
            System.out.println(S + 'G');
    }
}
