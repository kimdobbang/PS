import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = 1; // 생성자
        while (true) {

            // m>n 되면 생성자 못찾았으므로 0 출력
            if (n < m) {
                System.out.println(0);
                break;
            }

            // sum: 각자리 수의 합
            char[] nums = Integer.toString(m).toCharArray(); // int -> string -> array
            int sum = 0;
            for (char num : nums) {
                sum += num - '0'; // array 원소인 각 num은 string인데 정수로 바꾸기 위해 - '0'
            }

            // 입력값 == 생성자 + 각 자리 합이면 break
            if (n == m + sum) {
                System.out.println(m);
                break;

            // 아니면 다음 생성자 계산하기위해 m ++
            } else {
                m ++;
            }
        }
    }
}