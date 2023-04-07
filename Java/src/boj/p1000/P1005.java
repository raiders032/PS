package boj.p1000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

/**
 * https://www.acmicpc.net/problem/1005
 * 1005.ACM Craft
 * 풀이1.
 */
public class P1005 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(bufferedReader.readLine());

        while (testCase-- > 0) {
            StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int n = Integer.parseInt(stringTokenizer.nextToken());
            int k = Integer.parseInt(stringTokenizer.nextToken());
            List<Integer> times = Arrays.stream(bufferedReader.readLine().split(" "))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());

        }
    }
}
