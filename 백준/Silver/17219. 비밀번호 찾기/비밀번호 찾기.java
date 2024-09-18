//  비밀번호 찾기

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
		
	public static void main(String[] args) throws IOException{
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		HashMap<String, String> map = new HashMap<>();
		
		// 저장
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine()," ");
			String site = st.nextToken();
			String pw = st.nextToken();
			map.put(site, pw);
		}
		
		// 찾기
		for(int i = 0; i < M; i++) {
			String site = br.readLine();
			sb.append(map.get(site)).append("\n");
		}
		
		// 출력
		System.out.println(sb);
		
	} 
}
