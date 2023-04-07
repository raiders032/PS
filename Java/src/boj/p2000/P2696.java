package boj.p2000;
/*
https://www.acmicpc.net/problem/2696
2696.중앙값 구하기
골드2
풀이1.260ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P2696 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        while (tc-- > 0) {
            int n = Integer.parseInt(br.readLine());
            PriorityQueue<Integer> left = new PriorityQueue<>(Collections.reverseOrder());
            PriorityQueue<Integer> right = new PriorityQueue<>();
            List<Integer> answer = new ArrayList<>();

            for (int j = 0; j <= n / 10; j++) {
                StringTokenizer tokenizer = new StringTokenizer(br.readLine());
                for (int i = 1; tokenizer.hasMoreTokens(); i++) {
                    int num = Integer.parseInt(tokenizer.nextToken());
                    if (i % 2 == 1) {
                        if (left.isEmpty()) {
                            left.add(num);
                            answer.add(num);
                            continue;
                        }
                        if (num <= left.peek()) {
                            left.add(num);
                        } else {
                            right.add(num);
                            left.add(right.poll());
                        }
                        answer.add(left.peek());
                    } else {
                        if (left.peek() <= num) {
                            right.add(num);
                        } else {
                            left.add(num);
                            right.add(left.poll());
                        }
                    }
                }
            }

            System.out.println(answer.size());
            StringBuilder stringBuilder = new StringBuilder();
            for (int i = 1; i <= answer.size(); i++) {
                stringBuilder.append(answer.get(i - 1) + " ");
                if (i % 10 == 0) {
                    System.out.println(stringBuilder);
                    stringBuilder = new StringBuilder();
                }
            }
            System.out.println(stringBuilder);
        }
    }
}
