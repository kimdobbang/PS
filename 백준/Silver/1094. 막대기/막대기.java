import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();

        int cnt = 0;
        while (X > 0) {
            if ((X & 1) == 1) {
                cnt++;
            }
            X >>= 1;
        }

        System.out.println(cnt);
    }
}

/*
25
11001

23
10111

32
100000

64
1000000

48
110000



64
32/32
32
16/16
16/8/8
16/8/4/4
16/8/4
16/8/2/2
16/8/2
16/8/1/1
16/8/1


 */