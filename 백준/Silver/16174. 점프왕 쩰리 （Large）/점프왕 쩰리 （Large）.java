import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] arr;
	static boolean[][] visited;
	static int N;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N]; // 몇개인지 알때는 []해서 배열 쓰고 idx 사용. 모를때 arryList쓴다(get이 느려서)
		visited = new boolean[N][N];
		
		// 게임판 입력
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(bfs(0, 0) ? "HaruHaru" : "Hing");
	}
	
	// 젤리가 점프하며 탐색하는 메서드(bfs)
	static boolean bfs(int i, int j) {
		Deque<Point> dq = new ArrayDeque<>(); // 탐색할 아이들을 덱에 저장 
//		Point point = new Point();
//		point.x = i;
//		point.y = j;
//		dq.addLast(point);
		dq.addLast(new Point(i, j));
		visited[i][j] = true;
		
		while (!dq.isEmpty()) {
			Point now = dq.pollFirst();
			int dist = arr[now.r][now.c];
			// 오른쪽으로 이동
			int nr = now.r;
			int nc = now.c + dist;
			if (inMap(nr, nc) && !visited[nr][nc]) {
				dq.addLast(new Point(nr, nc));
				visited[nr][nc] = true;
				if (arr[nr][nc] == -1) {
					return true;
				}
			}
			// 아래쪽으로 이동
			nr = now.r + dist;
			nc = now.c;
			if (inMap(nr, nc) && !visited[nr][nc]) {
				dq.addLast(new Point(nr, nc));
				visited[nr][nc] = true;
				if (arr[nr][nc] == -1) {
					return true;
				}
			}
		}
		
		return false;
	}
	
	static boolean inMap(int nr, int nc) {
		return 0 <= nr && nr < N && 0 <= nc && nc < N;
	}
	
}

class Point {
	int r;
	int c;

	public Point(int r, int c) {
		this.r = r;
		this.c = c;
	}
}