/*
https://www.acmicpc.net/problem/14501
14501.퇴사
실버4
브루트포스,DP
 */
package boj.p14000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14501 {
    static int[] T;
    static int[] P;
    static int[] D;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int res = 0;
        T = new int[n];
        P = new int[n + 1];
        D = new int[n + 1];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            T[i] = Integer.parseInt(st.nextToken());
            P[i] = Integer.parseInt(st.nextToken());
        }

        for (int cur_day = 0; cur_day < n; cur_day++) {
            D[cur_day] = P[cur_day];
            for (int next_day = cur_day + T[cur_day]; next_day <= n; next_day++) {
                D[next_day] = Math.max(D[next_day], D[cur_day] + P[next_day]);
                res = Math.max(res, D[next_day]);
            }
        }
        System.out.println(res);


    }
}
