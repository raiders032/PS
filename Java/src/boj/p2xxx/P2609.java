package boj.p2xxx;

/*
https://www.acmicpc.net/problem/2609
2609.최대공약수와 최소공배수
실버5
풀이1.140ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2609 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        int num1 = Integer.parseInt(tokenizer.nextToken());
        int num2 = Integer.parseInt(tokenizer.nextToken());
        int gcd = getGCD(num1, num2);

        System.out.println(gcd);
        System.out.println(num1 * num2 / gcd);
    }

    public static int getGCD(int a, int b) {
        if (b == 0)
            return a;
        return getGCD(b, a % b);
    }
}
