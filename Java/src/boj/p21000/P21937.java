package boj.p21000;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

/**
 * https://www.acmicpc.net/problem/21937
 * 21937.작업
 * 풀이1.1052ms
 */
public class P21937 {
    private static Set<Integer> visit = new HashSet<>();
    private static List<List<Integer>> children;

    private static void visitChildren(int parent) {
        if (visit.contains(parent)) {
            return;
        }

        for (Integer child: children.get(parent)) {
            visitChildren(child);
            visit.add(child);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> input = Arrays.stream(bufferedReader.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        Integer n = input.get(0);
        children = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            children.add(new ArrayList<>());
        }

        for (int i = 0; i < input.get(1); i++) {
            List<Integer> vertexes = Arrays.stream(bufferedReader.readLine().split(" "))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());
            Integer child = vertexes.get(0);
            Integer parent = vertexes.get(1);
            children.get(parent).add(child);
        }

        int x = Integer.parseInt(bufferedReader.readLine());
        visitChildren(x);
        System.out.println(visit.size());
    }
}
