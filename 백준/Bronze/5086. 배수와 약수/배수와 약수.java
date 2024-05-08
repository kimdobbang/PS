import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//배수와 약수
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
        StringTokenizer st = new StringTokenizer(br.readLine());  // st는 1회용이라서 반복해서 사용하려면 반복문 안에 생성
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // 0 0 입력되면 멈춘다
            if (a + b == 0) {
                break;
            }

            if (b % a == 0) {
                sb.append("factor" + "\n");
            } else if (a % b == 0) {
                sb.append("multiple" + "\n");
            } else {
                sb.append("neither" + "\n");
            }
        }
        System.out.println(sb);
    }
}
