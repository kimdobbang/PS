import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int[] one = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        st = new StringTokenizer(br.readLine()," ");
        int[] two = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        st = new StringTokenizer(br.readLine()," ");
        int[] three = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};


        int x;
        int y;

        // x 좌표 비교 후 쌍을 이루지 않는 x 좌표 저장
        // 1번 x 와 2번 x 비교
        if (one[0] == two[0]) {
            x = three[0];
        }

        // 2번 x와 3번 x 비교
        else if (two[0] == three[0]) {
            x = one[0];
        }

        // 1번 x 와 3번 x 비교
        else {
            x = two[0];
        }


        // y좌 표 비교
        // 1번 y 와 2번 y 비교
        if (one[1] == two[1]) {
            y = three[1];
        }

        // 2번 y와 3번 y 비교
        else if (two[1] == three[1]) {
            y = one[1];
        }

        // 1번 y 와 3번 y 비교
        else {
            y = two[1];
        }

        System.out.println(x + " " + y);
        
    }
}
