import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double credit = 0;
        double score = 0;
        for (int i = 0; i < 20; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();
            double c = Double.parseDouble(st.nextToken());
            String grade = st.nextToken();
            double s = calc(grade);
            if (s == -1) {
                continue;
            }
            credit += c;
            score += c * s;
        }

        System.out.println(score / credit);
    }

    static double calc(String c) {
        double s = 0.5;
        switch(c) {
            case "A+":
                s += 0.5;
            case "A0":
                s += 0.5;
            case "B+":
                s += 0.5;
            case "B0":
                s += 0.5;
            case "C+":
                s += 0.5;
            case "C0":
                s += 0.5;
            case "D+":
                s += 0.5;
            case "D0":
                s += 0.5;
                break;
            case "F":
                s -= 0.5;
                break;
            case "P":
                return -1;
        }
        return s;
    }
}
