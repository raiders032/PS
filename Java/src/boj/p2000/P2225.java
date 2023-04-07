package boj.p2000;

/*
https://www.acmicpc.net/problem/2225
2225.합분해
골드5
풀이1.224ms
*/

import java.util.Scanner;

public class P2225 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();

        int[][] dp = new int[n + 1][k + 1];

        for (int i = 0; i <= n; i++) {
            dp[i][1] = 1;
        }

        for (int i = 0; i <= k; i++) {
            dp[0][i] = 1;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 2; j <= k; j++) {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000;
            }
        }

        System.out.println(dp[n][k]);
    }
}
