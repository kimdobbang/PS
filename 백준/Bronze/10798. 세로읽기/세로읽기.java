import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 세로읽기
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 띄어 쓰기가 없는 2차원 배열 생성 및 입력
        char[][] arr = new char[5][15];
        for (int i = 0; i < 5; i++) {
            String line = br.readLine();
            for (int j = 0; j < line.length(); j++) {
                arr[i][j] = line.charAt(j);
            }
        }

        // 확인
        for (int j = 0; j < 15; j++) {
            for (int i = 0; i < 5; i++) {
                if (arr[i][j] == 0){ // 캐릭터의 기본값이 아스키코드 0
                    continue;
                }
                sb.append(arr[i][j]);
            }
        }

        System.out.println(sb);
    }
}
