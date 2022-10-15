package boj.p18000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/*
https://www.acmicpc.net/problem/18233
18233.러버덕을 사랑하는 모임
실버1
풀이1.328ms
 */
public class P18233 {

    static int n, p, e;
    static Set<Integer> selectedIndex = new HashSet<>();
    static int[] x;
    static int[] y;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        x = new int[n];
        y = new int[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(st.nextToken());
            y[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0, 0, 0);
        System.out.println("-1");
    }

    static void dfs(int index, int minSum, int maxSum) {
        if (selectedIndex.size() == p) {
            if (e < minSum || e > maxSum)
                return;

            int[] answer = new int[n];

            for (int i = 0; i < n; i++) {
                if (selectedIndex.contains(i)) {
                    answer[i] = x[i];
                    e -= x[i];
                }
            }

            for (int i = 0; i < n; i++) {
                if (e > 0 && selectedIndex.contains(i)) {
                    int tmp = Math.min(e, y[i] - answer[i]);
                    answer[i] += tmp;
                    e -= tmp;
                }
                System.out.print(answer[i] + " ");
            }

            System.exit(0);
        }

        if (index == n)
            return;

        selectedIndex.add(index);
        dfs(index + 1, minSum + x[index], maxSum + y[index]);
        selectedIndex.remove(index);
        dfs(index + 1, minSum, maxSum);
    }
}
