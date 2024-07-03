// Text Roll
// package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            int n = Integer.parseInt(br.readLine());

            // 종료 조건
            if (n == 0) {
                System.out.println(sb);
                break;
            }

            // 종료 아닐 때
            else {
                int start = 0;
                int drop = 0;

                // 각 n줄 반복
                for (int i = 0; i < n; i++) {
                    String text = br.readLine();

                    // 시작점 찾기
                    for (int j = 0; j < text.length(); j++) {
                        if (text.charAt(j) != ' ') {
                            start = j;
                            break;
                        }
                    }

                    // 시작점 이후 문자열 순회
                    for (int j = drop; j < text.length(); j++) {
                        // 문장 끝까지 굴러가서 떨어짐
                        if (j == text.length() - 1) {
                            drop = start + j + 1;
                            break;
                        }
                        // 공백을 만나 떨어짐
                        if (text.charAt(j) == ' ' && j >= drop) {
                            drop = start + j;
                            break;
                        }
                    }
                }
                sb.append(drop + 1).append("\n");
            }
        }
    }
}