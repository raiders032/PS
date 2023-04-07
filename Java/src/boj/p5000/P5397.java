package boj.p5000;

/*
https://www.acmicpc.net/problem/5397
5397.키로거
실버3
풀이1.1012ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class P5397 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        while (tc-- > 0) {
            String password = br.readLine();
            Deque<Character> left = new LinkedList<>();
            Deque<Character> right = new LinkedList<>();

            for (char ch : password.toCharArray()) {
                if (ch == '<') {
                    if(left.size() > 0)
                        right.addFirst(left.pollLast());
                } else if (ch == '>') {
                    if(right.size() > 0)
                        left.addLast(right.pollFirst());
                } else if (ch == '-') {
                    if(left.size() > 0)
                        left.pollLast();
                } else {
                    left.addLast(ch);
                }
            }

            StringBuilder sb = new StringBuilder();
            for (Character ch: left){
                sb.append(ch);
            }

            for (Character ch: right){
                sb.append(ch);
            }

            System.out.println(sb.toString());
        }
    }
}
