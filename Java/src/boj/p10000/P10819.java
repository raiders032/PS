package boj.p10000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

/**
 * https://www.acmicpc.net/problem/10819
 * 10819.차이를 최대로
 * 풀이1.
 */
public class P10819 {
    private static int n;
    private static List<Integer> selected = new ArrayList<>();
    private static int answer = Integer.MIN_VALUE;
    private static int count = 0;

    private static void solveMaxTotalSum(Set<Integer> toVisit) {
        if (selected.size() == n) {
            count++;
            System.out.println("selected = " + selected);
            int result = 0;
            for (int i = 0; i < n - 1; i++) {
                result += Math.abs(selected.get(i) - selected.get(i + 1));
            }
            answer = Math.max(answer, result);
            return;
        }

        for (Integer current : new ArrayList<>(toVisit)) {
            toVisit.remove(current);
            selected.add(current);
            solveMaxTotalSum(toVisit);
            toVisit.add(current);
            selected.remove(selected.size() - 1);
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bufferedReader.readLine());
        List<Integer> numbers = Arrays.stream(bufferedReader.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        solveMaxTotalSum(new LinkedHashSet<>(numbers));
        System.out.println(answer);
        System.out.println("count = " + count);
    }
}
