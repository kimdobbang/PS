import java.util.Scanner;

// 시간제한1초, n이 최대 10,000 이므로 for문을 이용해 푼다
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        //for(int i=0; i<n; i++) //0,1,2가 (0 ~ n-1까지)아닌 1,2,3을 더하려는것(1~n)
        for(int i=1; i<=n; i++){
            sum += i; //sum에다 i를 계속 더하기
        }
        System.out.println(sum);
    }
}