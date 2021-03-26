/*
https://www.acmicpc.net/problem/1476
1476.날짜 계산
실버5
구현,수학,중국인의나머지정리
풀이1.128ms
 */
package boj.p1xxx;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1476 {
    static int E, S, M;
    static int e, s, m, year;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        E = Integer.parseInt(st.nextToken()) - 1;
        S = Integer.parseInt(st.nextToken()) - 1;
        M = Integer.parseInt(st.nextToken()) - 1;
        e = s = m = 0;
        year = 1;

        while (e != E || s != S || m != M ){
            e = (e + 1) % 15;
            s = (s + 1) % 28;
            m = (m + 1) % 19;
            year += 1;
        }

        System.out.println(year);
    }
}
