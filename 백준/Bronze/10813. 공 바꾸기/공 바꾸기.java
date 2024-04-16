import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); //바구니(공) 갯수
        int M = sc.nextInt(); //교환 횟수
        int[] arr = new int[N];

        //바구니 배열
        for (int i = 0; i < N; i++) {
            arr[i] = i + 1;
        }

        //공 M번 교환
        for (int k = 0; k < M; k++) {
            int i = sc.nextInt() - 1;
            int j = sc.nextInt() - 1;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

        //결과 출력
        for (int i : arr) {
            System.out.print(i + " ");
//            System.out.print(i + ' ');
        }
    }
}
