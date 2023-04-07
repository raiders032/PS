package boj.p9000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * https://www.acmicpc.net/problem/9081
 * 9081.단어 맞추기
 * 풀이1.120ms
 */
public class P9081 {
    public static char[] nextPermutation(char[] chars) {
        int n = chars.length;
        int i = n - 1;
        while (i > 0 && chars[i - 1] >= chars[i]) i--;

        if (i == 0) {
            return chars;
        }

        int j = n - 1;
        while (chars[i - 1] >= chars[j]) j--;

        char temp = chars[i - 1];
        chars[i - 1] = chars[j];
        chars[j] = temp;

        j = n - 1;
        while (i < j) {
            temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
            i++;
            j--;
        }

        return chars;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bufferedReader.readLine());
        for (int i = 0; i < n; i++) {
            String string = bufferedReader.readLine();
            char[] chars = string.toCharArray();
            System.out.println(nextPermutation(chars));
        }
    }

}
