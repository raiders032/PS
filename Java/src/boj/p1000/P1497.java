package boj.p1000;
/*
https://www.acmicpc.net/problem/1497
1497.기타콘서트
실버1
풀이1.184ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class P1497 {
    static long max_songs = 0;
    static Map<Integer, Long> guitars = new HashMap<>();
    static int answer = 100;
    static int n = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            st.nextToken();
            Long songs = 0L;
            for (char ch : st.nextToken().toCharArray()) {
                if (ch == 'Y')
                    songs = (songs << 1) + 1;
                else
                    songs <<= 1;
            }
            guitars.put(i, songs);
        }

        for (long i : guitars.values()) {
            max_songs |= i;
        }
        if (max_songs == 0) {
            System.out.println(-1);
        } else {
            dfs(0, 0, 0);
            System.out.println(answer);
        }
    }

    public static void dfs(int level, int count, long songs) {
        if (songs == max_songs) {
            answer = Math.min(answer, count);
            return;
        }

        if (level == n)
            return;

        dfs(level + 1, count + 1, songs | guitars.get(level));
        dfs(level + 1, count, songs);
    }
}
