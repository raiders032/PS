package boj.p2000;
/*
https://www.acmicpc.net/problem/2304
2304.창고 다각형
실버2
풀이1.156ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P2304 {

    static class Pair implements Comparable<Pair> {
        int x;
        int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Pair o) {
            return this.x - o.x;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Pair> pillars = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pillars.add(new Pair(x, y));
        }

        Collections.sort(pillars);
        int max_height = 0;
        int max_index = 0;
        for (int i = 0; i < pillars.size(); i++) {
            if (max_height < pillars.get(i).y) {
                max_height = pillars.get(i).y;
                max_index = i;
            }
        }

        Stack<Pair> left = new Stack<>();
        Stack<Pair> right = new Stack<>();
        int answer = max_height;

        for (int i = 0; i <= max_index; i++) {
            if (left.empty()) {
                left.push(pillars.get(i));
                continue;
            }

            if (left.peek().y <= pillars.get(i).y) {
                answer += left.peek().y * (pillars.get(i).x - left.peek().x);
                left.push(pillars.get(i));
            }
        }

        for (int i = n - 1; i >= max_index; i--) {
            if (right.empty()) {
                right.push(pillars.get(i));
                continue;
            }

            if (right.peek().y <= pillars.get(i).y) {
                answer += right.peek().y * (right.peek().x - pillars.get(i).x);
                right.push(pillars.get(i));
            }
        }
        System.out.println(answer);
    }
}
