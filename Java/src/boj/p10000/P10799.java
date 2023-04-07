package boj.p10000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

/**
 * https://www.acmicpc.net/problem/10799
 * 10799.쇠막대기
 * 풀이1.172ms
 */
public class P10799 {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        Deque<Character> stack = new ArrayDeque<>();
        char[] sequence = bufferedReader.readLine().toCharArray();
        int answer = 0;

        for (int i = 0; i < sequence.length; i++) {
            if (sequence[i] == '(') {
                stack.addLast(sequence[i]);
                continue;
            }
            stack.removeLast();
            if (i > 0 && sequence[i - 1] == '(') {
                answer += stack.size();
            } else {
                answer += 1;
            }

        }

        System.out.println(answer);
    }

}
