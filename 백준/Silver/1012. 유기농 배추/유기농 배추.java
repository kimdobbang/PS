import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	
	static boolean[][] visited;
	static boolean[][] map;
	static int N, M;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			// 맵 만들기
			map = new boolean[N][M];		
			for (int j = 0; j < K; j++) {
				st = new StringTokenizer(br.readLine());
				int c = Integer.parseInt(st.nextToken());
				int r = Integer.parseInt(st.nextToken());
				map[r][c] = true;
			}
			
			// 필요 지렁이 갯수 구하기
			visited = new boolean[N][M];
			int cnt = 0;
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < M; c++) {
					if(!visited[r][c] && map[r][c]) {
						bfs(r, c);
						cnt++;
					}
				}
			}
			
			System.out.println(cnt);
		}
	}
	
	static void bfs(int r, int c) {
		Deque<Point> dq = new ArrayDeque<Point>();
		dq.addLast(new Point(r,c));
		visited[r][c] = true;
		
		// 탐색 하는 반복문
		int[] dr = {0, 1, 0, -1};
		int[] dc = {1, 0, -1, 0};
		
		while(!dq.isEmpty()) {
			Point now = dq.pollFirst();
			
			for(int i = 0; i < 4; i++) {
				
				// 다음으로 이동할 지점
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];
				
				// 이동 가능여부 확인
				if (inMap(nr, nc) && !visited[nr][nc] && map[nr][nc]) {
					dq.addLast(new Point(nr, nc));
					visited[nr][nc] = true;
				}
			}
		}
	}
	
	static boolean inMap(int r, int c) {
		return 0 <= r && r < N && 0 <= c && c < M;
	}

}

class Point {
	int r;
	int c;
	
	public Point(int r, int c) {
		super();
		this.r = r;
		this.c = c;
	}
}