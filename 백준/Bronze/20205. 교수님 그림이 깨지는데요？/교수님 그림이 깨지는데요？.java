//교수님 그림이 깨지는데요?

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        // 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 계산 + 출력
        int[][] result = new int[n * k][n * k];
        for (int i = 0; i < n * k; i++) {
            for (int j = 0; j < n * k; j++) {
                sb.append(arr[i / k][j / k]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
        
//        //출력
//        for (int i = 0; i < n * k; i++) {
//            for (int j = 0; j < n * k; j++) {
//                System.out.print(result[i][j] + " ");
//            }
//            System.out.println();
//        }
    }
}
