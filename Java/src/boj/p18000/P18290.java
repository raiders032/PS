/*
https://www.acmicpc.net/problem/18290
18290.NM과 K (1)
실버1
풀이1.
 */
package boj.p18000;

import java.util.*;

public class P18290 {
    static int n, m, k;
    static Set<Integer> selected_num = new HashSet<>();
    static int res = -100000;
    static List<Integer> di;
    static int[][] board;

    static void dfs(int level, int index) {
        if (level == k) {
            int sum = 0;
            for (Integer number : selected_num) {
                sum += board[number / m][number % m];
            }
            res = Math.max(res, sum);
            return;
        }

        for (int i = index; i < n * m; i++) {
            boolean isOk = true;

            for (int dir = 0; dir < 2; dir++) {
                int next_i = i + di.get(dir);
                if (next_i < 0)
                    continue;
                if (selected_num.contains(next_i)) {
                    isOk = false;
                    break;
                }
            }
            if (!isOk)
                continue;
            selected_num.add(i);
            dfs(level + 1, i + 1);
            selected_num.remove(i);

        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        k = scanner.nextInt();
        board = new int[n][m];
        di = Arrays.asList(-1, -m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                board[i][j] = scanner.nextInt();
            }
        }
        dfs(0, 0);
        System.out.println(res);
    }
}
