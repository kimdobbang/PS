import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // 입력
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        // dp배열: 작은 값으로 바꿔 적을거니가 N개 칸을 N으로 채움. 최대 N이라서
        int[] dp = new int[1100];
        for (int i = 0; i < N; i++) {
            dp[i] = N;
        }
        // 계산
        dp[0] = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 1; j < arr[i] + 1; j++) {
                dp[i + j] = Math.min(dp[i + j], dp[i] + 1);
            }
        }
        if (dp[N-1] == N) {
            System.out.println(-1);
        } else {
            System.out.println(dp[N-1]);
        }
    }
}