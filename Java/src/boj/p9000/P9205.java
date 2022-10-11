package boj.p9000;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * https://www.acmicpc.net/problem/9205
 * 9205.맥주 마시면서 걸어가기
 * 풀이1.252ms
 */
public class P9205 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        int testCase = Integer.parseInt(bufferedReader.readLine());

        while (testCase-- > 0) {
            int n = Integer.parseInt(bufferedReader.readLine());

            List<int[]> position = new ArrayList();
            for (int i = 0; i < n + 2; i++) {
                StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
                int x = Integer.parseInt(stringTokenizer.nextToken());
                int y = Integer.parseInt(stringTokenizer.nextToken());
                position.add(new int[]{x, y});
            }

            boolean[][] distance = new boolean[n + 2][n + 2];
            for (int i = 0; i < n + 2; i++) {
                for (int j = 0; j < n + 2; j++) {
                    int[] xy1 = position.get(i);
                    int[] xy2 = position.get(j);
                    if (Math.abs(xy1[0] - xy2[0]) + Math.abs(xy1[1] - xy2[1]) <= 1000) {
                        distance[i][j] = true;
                        distance[j][i] = true;
                    }
                }
            }

            for (int i = 0; i < n + 2; i++) {
                for (int j = 0; j < n + 2; j++) {
                    for (int k = 0; k < n + 2; k++) {
                        if (distance[j][i] && distance[i][k]) {
                            distance[j][k] = true;
                        }
                    }
                }
            }

            if (distance[0][n + 1])
                bufferedWriter.write("happy\n");
            else
                bufferedWriter.write("sad\n");
        }
        bufferedWriter.flush();
        bufferedWriter.close();
        bufferedReader.close();
    }
}
