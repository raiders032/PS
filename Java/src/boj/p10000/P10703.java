package boj.p10000;

import java.io.*;
import java.util.*;

/**
 * https://www.acmicpc.net/problem/10703
 * 10703.유성
 * 풀이1.756ms
 */
public class P10703 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer input = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(input.nextToken());
        int m = Integer.parseInt(input.nextToken());
        Deque<int[]> stars = new ArrayDeque<>();
        char[][] board = new char[n][m];
        for (int i = 0; i < n; i++) {
            board[i] = bufferedReader.readLine().toCharArray();
        }

        int min_height = n - 1;
        for (int y = 0; y < m; y++) {
            int star = -1;
            int ground = n - 1;
            for (int x = 0; x < n; x++) {
                if (board[x][y] == 'X') {
                    star = x;
                    stars.addLast(new int[]{x, y});
                }
                if (board[x][y] == '#') {
                    ground = x;
                    break;
                }
            }
            if (star == -1)
                continue;
            min_height = Math.min(min_height, ground - star - 1);
        }

        while (!stars.isEmpty()) {
            int[] star = stars.removeLast();
            int x = star[0];
            int y = star[1];
            board[x][y] = '.';
            board[x + min_height][y] = 'X';
        }

        for (int i = 0; i < n; i++) {
            bufferedWriter.write(board[i]);
            bufferedWriter.newLine();
        }
        bufferedWriter.flush();
        bufferedWriter.close();
    }
}

/*
5 6
.XXXX.
...X..
...X..
#..###
######
---
5 6
.XX...
......
......
#..###
######
---
5 6
X.....
X.....
......
#..###
######
 */