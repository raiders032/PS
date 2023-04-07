package boj.p9000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


/**
 * https://www.acmicpc.net/problem/9024
 * 9024.두 수의 합
 * 풀이1.2056ms
 */
public class P9024 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(bufferedReader.readLine());
        StringTokenizer stringTokenizer;
        StringBuilder answer = new StringBuilder();

        while (testCase-- > 0) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int n = Integer.parseInt(stringTokenizer.nextToken());
            int k = Integer.parseInt(stringTokenizer.nextToken());

            int[] numbers = new int[n];
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for (int i = 0; i < n; i++) {
                numbers[i] = Integer.parseInt(stringTokenizer.nextToken());
            }
            Arrays.sort(numbers);

            int left = 0;
            int right = n - 1;
            int minDiff = Integer.MAX_VALUE;
            int count = 0;

            while (left < right) {
                int sum = numbers[left] + numbers[right];

                if (Math.abs(k - sum) < minDiff) {
                    minDiff = Math.abs(k - sum);
                    count = 1;
                } else if (Math.abs(k - sum) == minDiff) {
                    count++;
                }

                if (sum <= k) {
                    left++;
                } else {
                    right--;
                }
            }
            answer.append(count).append("\n");
        }
        System.out.println(answer);
    }
}
