package boj.p18000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * https://www.acmicpc.net/problem/18114
 * 18114.블랙 프라이데이
 * 풀이1.168ms
 */
public class P18114 {

    private static int binarySearch(int[] numbers, int target) {
        int low = -1;
        int high = numbers.length - 1;

        while (low + 1 < high) {
            int mid = (low + high) / 2;
            if (numbers[mid] < target)
                low = mid;
            else
                high = mid;
        }

        if (numbers[high] != target) {
            return -1;
        }

        return high;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int c = Integer.parseInt(stringTokenizer.nextToken());
        int answer = 0;

        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        Arrays.sort(numbers);

        if (binarySearch(numbers, c) != -1) {
            answer = 1;
        }

        if (answer != 1) {
            int left = 0;
            int right = n - 1;

            while (left < right) {
                int sum = numbers[left] + numbers[right];

                if (sum == c) {
                    answer = 1;
                    break;
                }

                int target = binarySearch(numbers, c - sum);
                if (target != -1 && numbers[target] != numbers[left] && numbers[target] != numbers[right]) {
                    answer = 1;
                    break;
                }

                if (sum < c)
                    left += 1;
                else
                    right -= 1;
            }
        }
        System.out.println(answer);
    }
}
