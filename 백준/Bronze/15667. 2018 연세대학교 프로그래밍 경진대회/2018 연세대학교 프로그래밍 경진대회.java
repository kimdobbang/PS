// 2018 연세대학교 프로그래밍 경진대회

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException{
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine()); // 불꽃갯수
		
		int K = 1;
		while(true) {
			int n = 1 + K + K * K;
			if(n == N) {
				break;
			}
			K++;
		}
		System.out.println(K);
	}
}
