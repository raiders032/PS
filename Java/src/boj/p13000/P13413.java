package boj.p13000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * https://www.acmicpc.net/problem/13413
 * 13413.오셀로 재배치
 * 풀이1.444ms
 */
public class P13413 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(bufferedReader.readLine());

        while (testCase-- > 0) {
            int n = Integer.parseInt(bufferedReader.readLine());
            char[] destination = bufferedReader.readLine().toCharArray();
            char[] source = bufferedReader.readLine().toCharArray();
            int count_wb = 0;
            int count_bw = 0;

            for (int i = 0; i < n; i++) {
                if (destination[i] == source[i])
                    continue;
                if (destination[i] == 'W') {
                    count_wb += 1;
                } else {
                    count_bw += 1;
                }
            }

            System.out.println(Math.max(count_wb, count_bw));
        }
    }
}
