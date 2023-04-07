/*
https://www.acmicpc.net/problem/3085
3085.사탕 게임
실버4
브루트포스,구현
풀이1.316ms
 */
package boj.p3000;

import java.util.Scanner;

public class P3085 {
    private static char[][] board;
    static int n;

    static int get_length(int x, int y) {
        int length = 0;
        int left = 1;
        int right = 1;

        while (x + right < n && board[x][y] == board[x + right][y]){
            right += 1;
        }
        while (x - left >= 0 && board[x][y] == board[x - left][y]){
            left += 1;
        }
        length = Math.max(length, left + right - 1);

        left = right = 1;
        while (y + right < n && board[x][y] == board[x][y + right]){
            right += 1;
        }
        while (y - left >= 0 && board[x][y] == board[x][y - left]){
            left += 1;
        }
        length = Math.max(length, left + right - 1);

        return length;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        board = new char[n][n];
        int res = 0;
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        for (int i = 0; i < n; i++) {
            board[i] = scanner.next().toCharArray();
        }

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                        continue;

                    if (board[x][y] == board[nx][ny]) {
                        res = Math.max(res, get_length(x, y));
                        continue;
                    }

                    char tmp = board[x][y];
                    board[x][y] = board[nx][ny];
                    board[nx][ny] = tmp;

                    res = Math.max(res, get_length(x, y));

                    tmp = board[x][y];
                    board[x][y] = board[nx][ny];
                    board[nx][ny] = tmp;

                }
            }
        }

        System.out.println(res);
    }
}
