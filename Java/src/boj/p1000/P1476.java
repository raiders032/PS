/*
https://www.acmicpc.net/problem/1476
1476.날짜 계산
실버5
구현,수학,중국인의나머지정리
풀이2.128ms
 */
package boj.p1000;

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
        year = s = m = E;


        while (s != S || m != M ){
            s = (s + 15) % 28;
            m = (m + 15) % 19;
            year += 15;
        }

        System.out.println(year + 1);
    }
}
