package boj.p9000;

/*
https://www.acmicpc.net/problem/9012
9012.괄호
실버4
풀이2.128ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int count = 0;
            String ps = br.readLine();

            for (char ch : ps.toCharArray()) {
                if (ch == '(') {
                    count += 1;
                } else {
                    if (count == 0) {
                        count = 1;
                        break;
                    }
                    count -= 1;
                }
            }

            if (count > 0) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }
    }
}
