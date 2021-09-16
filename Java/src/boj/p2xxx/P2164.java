package boj.p2xxx;

/*
https://www.acmicpc.net/problem/2164
2164.카드2
실버4
풀이1.288ms
 */

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class P2164 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            deque.addLast(i);
        }

        while (deque.size() >= 2) {
            deque.pollFirst();
            deque.addLast(deque.pollFirst());
        }

        System.out.println(deque.getFirst());
    }
}
