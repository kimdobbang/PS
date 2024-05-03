import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws IOException {
        // 점수표 데이터 입력
        Map<String, Double> scoreMap = new HashMap<>();
        scoreMap.put("A+", 4.5);
        scoreMap.put("A0", 4.0);
        scoreMap.put("B+", 3.5);
        scoreMap.put("B0", 3.0);
        scoreMap.put("C+", 2.5);
        scoreMap.put("C0", 2.0);
        scoreMap.put("D+", 1.5);
        scoreMap.put("D0", 1.0);
        scoreMap.put("F", 0.0);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double totalScore = 0; // 총점
        double totalCredit = 0; // 총 이수단위

        String str;
        // 입력이 끝날 때까지 반복하는 반복문!
        while((str=br.readLine()) != null) {
            String[] transcript = str.split(" "); // 입력받은 문자열 공백 기준으로 split해 배열 저장
            if (transcript.length != 3)
                break;

            double credit = Double.parseDouble(transcript[1]); // 과목의 이수단위
            String grade = transcript[2]; // 취득등급

            if (!grade.equals("P")) { // 성적이 P가 아닐 때만 계산
                double gradeValue = scoreMap.get(grade); //취득등급의 평점
                double score = credit * gradeValue; // 해당 과목 성적
                totalScore += score; // 전체 과목 성적의 합
                totalCredit += credit; // 전체 이수단위
            }
        }
        System.out.printf("%.6f", totalScore / totalCredit);
    }
}
