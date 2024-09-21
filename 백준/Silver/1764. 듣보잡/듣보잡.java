import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		HashSet<String> noListen = new HashSet<>();
		ArrayList<String> answer = new ArrayList<>();
        
        // 듣지못한애 저장
		for (int i = 0; i < n; i++) {
			noListen.add(br.readLine());
		}
        
        // 정답리스트에 보도못한애 중 듣지못한애 저장
		for (int i = 0; i < m; i++) {
			String s = br.readLine();
			if (noListen.contains(s)) {
				answer.add(s);
			}
		}
        
        //정렬
		Collections.sort(answer);
        
        
       // 출력
		sb.append(answer.size()).append("\n");
		for (String s : answer) {
			sb.append(s).append("\n");
		}
		System.out.println(sb);
	}
}
