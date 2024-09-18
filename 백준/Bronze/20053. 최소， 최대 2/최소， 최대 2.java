// 최소, 최대 2

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException{
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine()); //테케
		
		for (int t = 0; t < T; t++) {
			int N = Integer.parseInt(br.readLine()); // 정수 갯수
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int min = Integer.MAX_VALUE;
			int max = Integer.MIN_VALUE;
			for(int n = 0; n < N ; n++) {
				int num = Integer.parseInt(st.nextToken());
				if (num > max) {
					max = num;
				}
				if (num < min) {
					min = num;
				}
			}
            sb.append(min).append(" ").append(max).append("\n");
		}
		System.out.print(sb);
	}

}