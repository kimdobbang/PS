import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken()) * 100;
        int M = Integer.parseInt(st.nextToken());
        
        if (N >= M) System.out.print("Yes");
        else System.out.print("No");
    }
}