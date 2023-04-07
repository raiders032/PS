package boj.p11000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

/**
 * https://www.acmicpc.net/problem/11660
 * 11660.구간 합 구하기 5
 * 풀이1.1288ms
 */
public class P11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        int[][] prefixSum = new int[n][n];

        for (int i = 0; i < n; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for (int j = 0; j < n; j++) {
                prefixSum[i][j] = Integer.parseInt(stringTokenizer.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n; j++) {
                prefixSum[i][j] += prefixSum[i][j - 1];
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                prefixSum[i][j] += prefixSum[i - 1][j];
            }
        }

        for (int i = 0; i < m; i++) {
            List<Integer> position = Arrays.stream(bufferedReader.readLine().split(" "))
                    .map(x -> Integer.parseInt(x) - 1)
                    .collect(Collectors.toList());

            int result = prefixSum[position.get(2)][position.get(3)];
            if (position.get(0) > 0) {
                result -= prefixSum[position.get(0) - 1][position.get(3)];
            }
            if (position.get(1) > 0) {
                result -= prefixSum[position.get(2)][position.get(1) - 1];
            }
            if (position.get(0) > 0 && position.get(1) > 0) {
                result += prefixSum[position.get(0) - 1][position.get(1) - 1];
            }
            answer.append(result).append("\n");
        }
        System.out.println(answer);
    }
}
