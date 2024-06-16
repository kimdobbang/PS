// 삼각형과 세 변
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            int maxValue = Math.max(Math.max(a, b), c);
            int sub = a + b + c - maxValue;

            if (maxValue == 0) {
                break;
            }

            // 삼각형 아님
            if (maxValue >= sub) {
                System.out.println("Invalid");
                continue;
            }

            if (a == b && b == c) {
                System.out.println("Equilateral");
            } else if (a != b && b != c && a != c) {
                System.out.println("Scalene");
            } else {
                System.out.println("Isosceles");
            }

        }
    }
}
