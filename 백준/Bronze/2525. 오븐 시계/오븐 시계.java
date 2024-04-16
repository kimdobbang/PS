import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();
        int T = sc.nextInt();
        int hour;
        int min;

        // hour 안바뀜
        if (M + T < 60){
            min = M + T;
            hour = H;
        }

        //hour 바뀜
        else {
            min = (M + T) % 60;
            hour = H + (M + T)/60;
            //24시 넘을경우
            if (hour >= 24){
                hour -= 24;
            }
        }
        System.out.println(hour + " " + min);
    }
}
