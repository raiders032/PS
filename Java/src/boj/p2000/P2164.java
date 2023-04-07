package boj.p2000;

/*
https://www.acmicpc.net/problem/2164
2164.카드2
실버4
풀이2.288ms
 */

import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class P2164 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Deque<Integer> deque = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            deque.addLast(i);
        }

        while (deque.size() > 1) {
            deque.pollFirst();
            deque.addLast(deque.pollFirst());
        }

        System.out.println(deque.pollLast());
    }
}
