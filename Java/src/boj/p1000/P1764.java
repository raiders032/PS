package boj.p1000;
/*
https://www.acmicpc.net/problem/1764
1764.듣보잡
실버4
풀이1.432ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P1764 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Set<String> names = new HashSet<>();
        List<String> answer = new ArrayList<>();

        for (int i = 0; i < n + m; i++) {
            String name = br.readLine();

            if (names.contains(name)) {
                answer.add(name);
            } else {
                names.add(name);
            }
        }

        Collections.sort(answer);
        System.out.println(answer.size());

        for (String name : answer) {
            System.out.println(name);
        }
    }
}
