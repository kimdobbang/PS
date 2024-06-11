import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 구간 합 구하기 4
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); //5
        int M = Integer.parseInt(st.nextToken()); //3
        int[] numbers = new int[N];
        int[] prefixSum = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken()); // 5 4 3 2 1
            prefixSum[i + 1] += prefixSum[i] + numbers[i];
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

           int result = prefixSum[b] - prefixSum[a - 1];
            System.out.println(result);

        }
    }
}
