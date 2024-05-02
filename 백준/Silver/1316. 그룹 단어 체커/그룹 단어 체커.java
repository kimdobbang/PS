import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 그룹 단어 체커
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        int ans = 0;
        for (int t = 0; t < T; t++) {
        char[] chars = br.readLine().toCharArray();

            int cnt = 1; //정렬 전 문자열 바뀔때마다 count. 1부터 시작하므로 초기값 1
            int group = 1; // 그룹 알기위해 정렬해서 문자 바뀔 때마다 count

            if (chars.length == 1) {
                cnt += 0;
            }
            else {
                for (int i = 1; i < chars.length; i++) {
                    if (chars[i] != chars[i - 1]) {
                        cnt ++;
                    }
                }//정렬 전 for
                
                Arrays.sort(chars);
                for (int i = 1; i < chars.length; i++) {
                    if (chars[i] != chars[i - 1]) {
                        group ++;
                    }
                }//정렬 후 for
            }//else
            
            // 정렬 전 후가 같다면 그룹임
            if (cnt==group) {
                ans ++;
            }
        }
        System.out.println(ans);
    }
}
