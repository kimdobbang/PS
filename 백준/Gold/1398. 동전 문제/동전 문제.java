import java.util.Scanner;

// 동전문제
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //1~99까지 필요한 동전 갯수 dp
        int[] dp = new int[100];
        for (int i = 0; i < 10; i++) {
            dp[i] = i;
        }
        for (int i = 10; i < 25; i++) {
            dp[i] = Math.min(dp[i-1] + 1, dp[i-10] + 1);
        }
        for (int i = 25; i < 100; i++) {
            dp[i] = Math.min(Math.min(dp[i-1] + 1, dp[i-10] + 1), dp[i-25] + 1);
        }

        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            long P = sc.nextLong();
            //테스트 케이스 100단위 형태로 바꾸기
            int res = 0;
            while (P>0) {
                res += dp[(int)(P % 100)];
                P /= 100;
            }
            System.out.println(res);
        }
    }
}
