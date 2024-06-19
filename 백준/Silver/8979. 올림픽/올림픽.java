// 올림픽
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 데이터 입력(국가번호: 인덱스)
        int [][] arr = new int[N + 1][3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int id = Integer.parseInt(st.nextToken());
            for (int j = 0; j < 3; j++) {
                arr[id][j] = Integer.parseInt(st.nextToken());
            }
        }

        // K국가와 등수 비교
        int cnt = 0;
        for (int i = 1; i < N + 1; i++) {
            // 금 많은국가
            if (arr[K][0] < arr[i][0]) {
                cnt++;
                //금 동점일때
            } else if (arr[K][0] == arr[i][0]) {
                // 은 많은국가
                if (arr[K][1] < arr[i][1]) {
                    cnt++;
                // 은 동점일 때
                } else if (arr[K][1] == arr[i][1]) {
                    // 동 많은 국가
                    if (arr[K][2] < arr[i][2]) {
                        cnt++;
                    }
                }
            }
        }

        System.out.println(cnt + 1);

    }
}
