import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int burger = Math.min(A, Math.min(B, C));

        int co = sc.nextInt();
        int ci = sc.nextInt();
        int drink = Math.min(co, ci);

        System.out.println(burger + drink - 50);
    }
}
