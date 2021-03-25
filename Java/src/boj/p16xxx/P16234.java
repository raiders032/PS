/*
https://www.acmicpc.net/problem/16234
16234.인구 이동
골드5
BFS,그래프이론,그래프탐색,구현,시뮬레이션
풀이1.964ms
*/
package boj.p16xxx;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class P16234 {
    static int[][] board;
    static int n, l, r;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    static class Nation {
        int x;
        int y;

        public Nation(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static boolean move(int x, int y) {
        Queue<Nation> queue = new LinkedList<>();
        ArrayList<Nation> union = new ArrayList<>();
        queue.add(new Nation(x, y));
        visited[x][y] = true;
        int count = 0;
        int population = 0;

        while (!queue.isEmpty()) {
            Nation nation = queue.poll();
            union.add(nation);
            x = nation.x;
            y = nation.y;
            count += 1;
            population += board[x][y];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                    continue;

                if (visited[nx][ny])
                    continue;

                int diff = Math.abs(board[x][y] - board[nx][ny]);
                if (diff < l || diff > r)
                    continue;

                visited[nx][ny] = true;
                queue.add(new Nation(nx, ny));
            }

        }

        for (Nation nation : union) {
            board[nation.x][nation.y] = population / count;
        }

        return union.size() != 1;
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        l = scanner.nextInt();
        r = scanner.nextInt();
        board = new int[n][n];
        visited = new boolean[n][n];
        int res = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = scanner.nextInt();
            }
        }

        while (true) {
            boolean is_moved = false;
            visited = new boolean[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visited[i][j])
                        continue;
                    if (move(i, j))
                        is_moved = true;
                }
            }

            if (!is_moved)
                break;
            else
                res += 1;
        }
        System.out.println(res);
    }
}
