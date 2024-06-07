import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

// 세금
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int prize = Integer.parseInt(br.readLine());
        System.out.println((int) (prize * 0.78) + " " + (int) (prize * 0.8 + prize * 0.2 * 0.78));
    }
}
