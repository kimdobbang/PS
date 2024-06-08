import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 뜨거운 붕어빵
public class Main{
    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

//        int[] arr = new int[5];
        char[][] lst = new char[n][m];
//        lst[0][0], lst[0][1]
//        for (int i = 0; i < n; i++) {
//            st = new StringTokenizer(br.readLine());
//            for (int j = 0; j < m; j++) {
//                lst[i][j] = st.nextToken().charAt(0);
//            }
//        }
        for (int i = 0; i < n; i++) {
            lst[i] = br.readLine().toCharArray();
        }

        for (int i = 0; i < n; i++) {
            for (int j = m-1; j >= 0 ; j--) {
                System.out.print(lst[i][j]);
            }
            System.out.println();
        }
    }
}
