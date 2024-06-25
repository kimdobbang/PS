// Absolutely

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
//        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            double x = Double.parseDouble(st.nextToken());
            double y = Double.parseDouble(st.nextToken());
//            double diff = Math.round(Math.abs(x - y) * 10) / (double) 10;
//            sb.append(String.format("%.1f", diff)).append("\n");
            System.out.printf("%.1f\n", Math.abs(x - y));
        }
    }
}
