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
		HashSet<String> noSee = new HashSet<>();

		for (int i = 0; i < n; i++) {
			noListen.add(br.readLine());
		}

		for (int i = 0; i < m; i++) {
			noSee.add(br.readLine());
		}

		ArrayList<String> answer = new ArrayList<>();
		for (String s : noListen) {
			if (noSee.contains(s)) {
				answer.add(s);
			}
		}

		Collections.sort(answer);

		sb.append(answer.size()).append("\n");
		for (String s : answer) {
			sb.append(s).append("\n");
		}

		System.out.println(sb);
	}
}
