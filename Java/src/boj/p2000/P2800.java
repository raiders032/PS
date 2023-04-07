package boj.p2000;

import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

/*
https://www.acmicpc.net/problem/2800
2800.괄호 제거
골드5
풀이1.
 */
public class P2800 {
    static Set<String> exps = new TreeSet<>();
    static int leftCount = 0;
    static int rightCount = 0;
    static String exp = null;

    public static void main(String[] args) {
        exp = new Scanner(System.in).next();
        dfs("", 0, 0, 0);
        exps.remove(exp);
        exps.stream().forEach((e) -> System.out.println(e));
    }

    public static void dfs(String string, int index, int leftCount, int rightCount) {
        if (index == exp.length()) {
            if (leftCount == rightCount)
                exps.add(string);
            return;
        }

        if (exp.charAt(index) != '(' && exp.charAt(index) != ')') {
            dfs(string + exp.charAt(index), index + 1, leftCount, rightCount);
            return;
        }

        if (exp.charAt(index) == '(' && leftCount == rightCount)
            dfs(string + exp.charAt(index), index + 1, leftCount + 1, rightCount);

        if (exp.charAt(index) == ')' && leftCount - 1 == rightCount)
            dfs(string + exp.charAt(index), index + 1, leftCount, rightCount + 1);
        dfs(string, index + 1, leftCount, rightCount);
    }
}
