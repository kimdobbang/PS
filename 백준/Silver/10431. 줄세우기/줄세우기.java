// 줄세우기

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int P = Integer.parseInt(br.readLine());
        
        // 입력
        for (int i = 1; i < P + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();
            int[] students = new int[20];

            // students 데이터 입력
            for (int j = 0; j < 20; j++) {
                 students[j] = Integer.parseInt(st.nextToken());
            }

            // 정렬 및 결과 계산
            int result = 0;
            ArrayList<Integer> sorted = new ArrayList<>();

            sorted.add(students[0]);
            o: for (int j = 1; j < 20; j++) {
                int now = students[j];

                // arrayList에서 자기 앞에 자기보다 키가 큰 학생 있는지 확인
                for (int k = 0; k < j; k++) {
                    if (sorted.get(k) > now) {
                        sorted.add(k, now);
                        // 걔 앞에 애들 한 걸음씩 물러남
                        result += j - k;
                        continue o;
                    }
                }
                // 자기보다 큰 학생이 없었다면 맨 뒤에 선다
                sorted.add(now);
            }
            System.out.println(i + " " + result);
        }
    }
}
