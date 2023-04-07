package boj.p10000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * https://www.acmicpc.net/problem/10164
 * 10164.격자상의 경로
 * 풀이1.424ms
 */
public class P10164 {
    private static int getPath(int x, int y, int target, int currentPosition, boolean isValid) {
        if ((target < currentPosition && !isValid) || x * y <= currentPosition) {
            return 0;
        }

        if (currentPosition == x * y - 1) {
            return 1;
        }

        int result = 0;
        isValid = currentPosition == target ? true : isValid;

        if ((currentPosition + 1) % y != 0) {
            result += getPath(x, y, target, currentPosition + 1, isValid);
        }

        if (currentPosition + y < x * y) {
            result += getPath(x, y, target, currentPosition + y, isValid);
        }

        return result;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> input = Arrays.stream(bufferedReader.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        System.out.println(getPath(input.get(0), input.get(1), input.get(2) - 1 < 0 ? 0 : input.get(2) - 1, 0, false));
    }
}
