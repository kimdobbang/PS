// 듣보잡
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		HashMap<String, Integer> map = new HashMap<>();
		TreeSet<String> resultSet = new TreeSet<>();

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		// map으로 카운팅
		for (int i = 0; i < N + M; i++) {
			String name = br.readLine();
			map.put(name, map.getOrDefault(name, 0)+1);
		}

		// 2인 애들만 정렬하는 셋에 넣음
		for (String name : map.keySet()) {
			if (map.get(name) == 2) {
				resultSet.add(name);
			}
		}

		// 출력
		sb.append(resultSet.size()).append("\n");
		for (String name : resultSet) {
			sb.append(name).append("\n");
		}
		System.out.println(sb);

	}
}
