import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt(); // 1 <= year <= 4000 이라서 int로 받아도 무방
        //연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            System.out.println("1");
        } else {
            System.out.println("0");
        }
    }
}
