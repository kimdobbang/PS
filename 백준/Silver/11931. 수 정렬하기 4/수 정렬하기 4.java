//수 정렬하기 4

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * -1_000_000 ~ 1_000_000 -> 2_000_001
         * 0 ~ 2_000_000 -> 2_000_001
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        // + 1,000,000 으로 만든 배열 생성
        boolean[] arr = new boolean[2_000_001];
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[num + 1_000_000] = true;
        }

        // 인덱스 - 1_000_000 해서 출력
        for (int i = 2_000_000; i >= 0; i--) {
            if (arr[i] == true) {
                sb.append(i - 1_000_000).append("\n");
//                System.out.println(i -  1_000_000);
            }
        }
        System.out.println(sb);
    }
}
