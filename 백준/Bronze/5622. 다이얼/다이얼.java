import java.io.IOException;

// 다이얼
// 해당 조건 내에서의 값만 입력(즉, 예외 값 입력되지 않음)되므로 따로 생성 없이 우너시입력을 받아 문자열 값만 알아내어 count
public class Main {
    public static void main(String[] args) throws IOException {

        int count = 0;
        int value;

        while (true) {

            value = System.in.read();
            if (value == '\n') {
                break;
            }

            if (value < 68) count += 3;
            else if (value < 71) count += 4;
            else if (value < 74) count += 5;
            else if (value < 77) count += 6;
            else if (value < 80) count += 7;
            else if (value < 84) count += 8;
            else if (value < 87) count += 9;
            else count += 10;

        }
        System.out.println(count);
    }
}
