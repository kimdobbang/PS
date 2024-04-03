import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int check =sc.nextInt();
        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (check == sc.nextInt())
                cnt++;
        }
        System.out.println(cnt);
    }
}
