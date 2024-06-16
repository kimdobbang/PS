// 연속구간
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 3; i++) {
            String numbers = "0" + br.readLine();

            int maxValue = 1;
            int cnt = 1;

            for (int j = 1; j < 9; j++) {
                if (numbers.charAt(j) == numbers.charAt(j - 1)) {
                    cnt++;
                    maxValue = Math.max(maxValue, cnt);
                }
                else {
                    cnt = 1;
                }
            }
            System.out.println(maxValue);
        }
    }
}
