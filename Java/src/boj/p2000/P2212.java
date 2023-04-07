package boj.p2000;

/*
https://www.acmicpc.net/problem/2212
2212.센서
골드5
풀이1.256ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class P2212 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int answer = 0;

        Integer[] nums = new Integer[n];
        Integer[] diff = new Integer[n - 1];
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(tokenizer.nextToken());
        }

        Arrays.sort(nums);
        for (int i = 0; i < n - 1; i++) {
            diff[i] = nums[i + 1] - nums[i];
        }

        Arrays.sort(diff, Collections.reverseOrder());

        for (int i = k - 1; i < n - 1; i++) {
            answer += diff[i];
        }

        System.out.println(answer);
    }
}
