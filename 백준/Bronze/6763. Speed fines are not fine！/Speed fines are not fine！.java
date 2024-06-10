import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int limit = Integer.parseInt(br.readLine());
        int speed = Integer.parseInt(br.readLine());
        int over = speed - limit;
        int fine;

        if (over <= 0) {
            System.out.println("Congratulations, you are within the speed limit!");
        } else {
            if (over <= 21) {
                fine = 100;
            } else if (over <= 30) {
                fine = 270;
            } else {
                fine = 500;
            }
            System.out.println("You are speeding and your fine is $" + fine + "." );
        }
    }
}