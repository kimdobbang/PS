import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int fac = 1;
        for (int n = N; n > 0 ; n--) {
            fac *= n;
        }
        System.out.println(fac);
    }
}