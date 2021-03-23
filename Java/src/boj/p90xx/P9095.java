/*
https://www.acmicpc.net/problem/9095
9095.1, 2, 3 더하기
실버3
DP
풀이1.244ms
 */
package boj.p90xx;

import java.util.Scanner;

public class P9095 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] dp = new int[11];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i = 4; i <= 10; i++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
        }

        for (int i = 0; i < n; i++) {
            int num = scanner.nextInt();
            System.out.println(dp[num]);
        }

    }
}
