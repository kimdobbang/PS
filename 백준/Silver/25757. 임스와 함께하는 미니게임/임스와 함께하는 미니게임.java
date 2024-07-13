// 임스와 함께하는 미니게임

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        String game = st.nextToken();
        HashMap<String, Integer> limit = new HashMap<>();
        limit.put("Y", 2);
        limit.put("F", 3);
        limit.put("O", 4);

        // 사람들 중복 없이 저장
        HashSet<String> player = new HashSet<>();
        for (int i = 0; i < N; i++) {
            player.add(br.readLine());
        }
        System.out.println(player.size() / (limit.get(game) - 1));
    }
}
