import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        //손익분기점: 비용 < 매출 일 때
        // A + B * q < C * q
        // 손익분기점이 없는 경우? : B >= C인 경우

        // 매출이 비용보다 작거나 같은 경우
        if (C - B <= 0) {
            System.out.println(-1);
        }

        // 아니면 손익분기점 + 1개 더 판매한 판매량 출력
        else {
            int bep = A / (C - B); // 손익분기점
            System.out.println( bep + 1 );
        }
    }
}
