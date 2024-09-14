import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		int cnt = 0;
		int pre_str = 32;
		int now_str;

		while (true) {
			// 현재문자
			now_str = System.in.read();

			// 현재 공백 && 이전문자 공백아님
			if (now_str == 32 && pre_str != 32) {
				cnt++;
			}

			// 현재 문자 줄바꿈 && 이전 문자 공백 아님(공백일땐 앞의 조건문에서 cnt+1처리)
			else if (now_str == 10) {
				if (pre_str != 32) {
					cnt++;
				}
				break;
			}
			// 이전문자에 현재문자
			pre_str = now_str;
		}
		System.out.println(cnt);
	}
}