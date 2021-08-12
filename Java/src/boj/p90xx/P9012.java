package boj.p90xx;

/*
https://www.acmicpc.net/problem/9012
9012.괄호
실버4
풀이1.144ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            char[] ps = br.readLine().toCharArray();
            int count = 0;

            for (char p : ps) {
                if (p == '(')
                    count += 1;

                else if (count < 1) {
                    count = 1;
                    break;
                } else
                    count -= 1;
            }

            if (count > 0)
                System.out.println("NO");
            else
                System.out.println("YES");
        }
    }
}
