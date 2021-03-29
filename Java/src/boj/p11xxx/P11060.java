package boj.p11xxx;

/*
https://www.acmicpc.net/problem/11060
11060.점프 점프
실버2
DPx
풀이1.304ms
*/

import java.util.Arrays;
import java.util.Scanner;

public class P11060 {
    static int n;
    static int[] array;
    static int[] dp;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        array = new int[n];
        dp = new int[n];
        Arrays.fill(dp, 10000);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            array[i] = scanner.nextInt();
        }

        for (int index = 0; index < n; index++) {
            for (int next = index + 1; next < n && next <= index + array[index]; next++) {
                dp[next] = Math.min(dp[next], dp[index] + 1);
            }
        }

        if(dp[n-1] == 10000)
            System.out.println(-1);
        else
            System.out.println(dp[n - 1]);

    }

}
