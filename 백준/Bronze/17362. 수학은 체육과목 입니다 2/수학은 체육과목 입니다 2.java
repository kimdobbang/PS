import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        N %= 8;
        switch (N) {
            case 0:
                N = 2;
                break;
            case 6:
                N = 4;
                break;
            case 7:
                N = 3;
        }
        System.out.println(N);
    }
}