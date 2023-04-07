package boj.p11000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
https://www.acmicpc.net/problem/11675
11675.Jumbled Communication
실버5
풀이1.400ms
 */
public class P11675 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());

            for (int j = 0; j <= 255; j++) {
                if ((j ^ (j << 1) & 255) == num) {
                    System.out.println(j);
                    break;
                }
            }
        }
    }
}
