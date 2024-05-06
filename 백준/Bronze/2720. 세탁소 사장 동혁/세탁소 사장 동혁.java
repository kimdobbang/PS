// 세탁소 사장 동혁

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {

            int C = Integer.parseInt(br.readLine());
            int Q = 0; // 25
            int D = 0; // 10
            int N = 0; // 5
            int P = 0; // 1

            while (C > 0) {
                Q += C / 25;
                C %= 25;

                D += C / 10;
                C %= 10;

                N += C / 5;
                C %= 5;

                P += C;
                C = 0;

            }
            sb.append(Q + " " + D + " " + N + " " + P + "\n");
//            System.out.println(Q + " " + D + " " + N + " " + P);
        }
            System.out.println(sb);

    }
}
