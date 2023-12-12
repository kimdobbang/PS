import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double A = sc.nextInt();
        double B = sc.nextInt();
//        float A = sc.nextInt();
//        float B = sc.nextInt();
        System.out.println(A/B);
        // float double => 정밀도 차이남
        // float : 소수점 6~7자리 정도?
        // double: 소수점 15~16자리 정도까지 표현 가능
        // 문제의 '10^-9 이하의 오차 허용한다'는 double로는 괜찮다. 라는 뜻
        // TODO 코딩테스트에서는 웬만하면 float보다 double 쓰는게 더 좋다.
    }
}