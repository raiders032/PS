package boj.p12000;
/*
https://www.acmicpc.net/problem/12813
12813.이진수 연산
브론즈2
풀이1.508ms
 */

import java.util.Scanner;

public class P12813 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char[] a = scanner.next().toCharArray();
        char[] b = scanner.next().toCharArray();
        StringBuilder sb = null;

        sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            if (a[i] == '0' || b[i] == '0')
                sb.append("0");
            else
                sb.append("1");
        }
        System.out.println(sb);

        sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            if (a[i] == '1' || b[i] == '1')
                sb.append("1");
            else
                sb.append("0");
        }
        System.out.println(sb);

        sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            if (a[i] == b[i])
                sb.append("0");
            else
                sb.append("1");
        }
        System.out.println(sb);

        sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            if (a[i] == '1')
                sb.append("0");
            else
                sb.append("1");
        }
        System.out.println(sb);

        sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            if (b[i] == '1')
                sb.append("0");
            else
                sb.append("1");
        }
        System.out.println(sb);
    }
}
