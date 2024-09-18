import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int t = 0; t < T; t++) {
			long lt = sc.nextInt();
			long wt = sc.nextInt();
			long le = sc.nextInt();
			long we = sc.nextInt();
			
			if (lt * wt > le * we) {
                System.out.println("TelecomParisTech");  // TelecomParisTech 출력
            } else if (lt * wt < le * we) {
                System.out.println("Eurecom");  // Eurecom 출력
            } else {
                System.out.println("Tie");  // 면적이 같으면 Tie 출력
            }
		}
		
	}

}
