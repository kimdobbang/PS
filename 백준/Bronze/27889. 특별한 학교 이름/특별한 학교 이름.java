// 특별한 학교 이름

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		String school = br.readLine();
		String fullname = "";
		switch (school) {
			case "NLCS": fullname = "North London Collegiate School";
			break;
			case "BHA": fullname = "Branksome Hall Asia";
			break;
			case "KIS": fullname = "Korea International School";
			break;
			case "SJA": fullname = "St. Johnsbury Academy";
			break;
			default: fullname = "Unknown School"; 
		}
		sb.append(fullname);
		System.out.println(sb);
	}
}
