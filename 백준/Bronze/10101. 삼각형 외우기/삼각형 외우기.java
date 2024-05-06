import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 삼각형 외우기
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());
        int sumVal = A + B + C;

        if (A == 60 && B == 60 && C == 60) {
            sb.append("Equilateral");
        }
        else if ((sumVal == 180) && (A == B || A == C || B == C)) {
            sb.append("Isosceles");
        }
        else if ((sumVal == 180) && (A != B && A != C && B != C)) {
            sb.append("Scalene");
        }
        else {
            sb.append("Error");
        }
        System.out.println(sb);
    }
}
