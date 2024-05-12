import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 피자(small)
public class Main {

    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        pizza(N);
        System.out.println(result);
    }

    static void pizza(int N) {
        if (N == 1) {
            return;
        }
        int b = N / 2;
        int c = N - b;
        result += b * c;
        pizza(b);
        pizza(c);
    }
}
