// if 아래 esle if 가 아닌 else를 사용 했어도됨(수정) 조건이 +, - 두가지라서

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        if (x > 0) {
            if (y > 0) {
                System.out.println("1");
            } else {
                System.out.println("4");
            }
        }else {
            if (y > 0) {
                System.out.println("2");
            } else {
                System.out.println("3");
            }
        }
    }
}