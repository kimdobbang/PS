//헤라클레스와 히드라

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());

        // 테스트케이스 순회
        for (int i = 1; i <= K; i++) {
            int h = Integer.parseInt(br.readLine()); // 머리 갯수
            String actions = br.readLine();

            int b = 0; // 머리 자르고 + 불 지짐
            int c = 0; // 머리만 자름

            // 헤라클레스의 행동 순회
            for (int j = 0; j < actions.length(); j++) {
                if (actions.charAt(j) == 'c'){
                    c++;
                }
                else b++;
            }

            int hdr = h + (c * 2); // 전체 머리 총 합
            int cut = b + c; // 자른 머리 총 합
            System.out.println("Data Set " + i + ":");
            System.out.println(hdr - cut);
            if (i != K) {
            System.out.println();
            }
        }
    }
}
