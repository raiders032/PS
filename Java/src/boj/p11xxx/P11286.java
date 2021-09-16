package boj.p11xxx;

/*
https://www.acmicpc.net/problem/11286
11286.절댓값 힙
실버1
풀이1.660ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class P11286 {

    static class Value implements Comparable<Value> {

        int num;
        int abs;

        public Value(int num, int abs) {
            this.num = num;
            this.abs = abs;
        }

        @Override
        public int compareTo(Value o) {
            if (this.abs == o.abs) {
                return this.num - o.num;
            } else {
                return this.abs - o.abs;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Value> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());

            if (num == 0) {
                if (pq.size() != 0) {
                    Value value = pq.poll();
                    System.out.println(value.num);
                } else {
                    System.out.println(0);
                }
            } else {
                pq.add(new Value(num, Math.abs(num)));
            }
        }
    }
}
