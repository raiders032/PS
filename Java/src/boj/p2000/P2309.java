/*
https://www.acmicpc.net/problem/2309
2309번 일곱 난쟁이
브론즈2
브루트포스 알고리즘
풀이1.132
*/
package boj.p2000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P2309 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = 9;
        int[] heights = new int[n];
        int sum = 0;

        for (int i = 0; i < n; i++) {
            heights[i] = Integer.parseInt(br.readLine());
            sum += heights[i];
        }

        Arrays.sort(heights);

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (heights[i] + heights[j] == sum - 100) {
                    for (int k = 0; k < n; k++) {
                        if (k == i || k == j)
                            continue;
                        System.out.println(heights[k]);
                    }
                    return;
                }
            }
        }

    }
}
