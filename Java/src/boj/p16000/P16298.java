package boj.p16000;
/*
https://www.acmicpc.net/problem/16928
16928.뱀과 사다리 게임
실버1
풀이1.X
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P16298 {
    static Map<Integer, Integer> ladderAndSnake = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());

        for (int i = 0; i < n + m; i++) {
            tokenizer = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(tokenizer.nextToken());
            int end = Integer.parseInt(tokenizer.nextToken());

            ladderAndSnake.put(start, end);
        }

        System.out.println(solve());
    }

    public static int solve() {
        Queue<Pair> queue = new LinkedList<>();
        boolean[] visited = new boolean[101];

        visited[1] = true;
        queue.add(new Pair(1, 0));

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            int location = pair.location;
            int count = pair.count;
            if (location == 100) {
                return count;
            }

            for (int dice = 1; dice <= 6; dice++) {
                int nextLocation = location + dice;

                if (nextLocation > 100)
                    break;

                if (visited[nextLocation])
                    continue;

                while (true) {
                    if (ladderAndSnake.containsKey(nextLocation)) {
                        visited[nextLocation] = true;
                        queue.add(new Pair(nextLocation, count + 1));
                        nextLocation = ladderAndSnake.get(nextLocation);
                        if (visited[nextLocation])
                            break;
                        continue;
                    }
                    visited[nextLocation] = true;
                    queue.add(new Pair(nextLocation, count + 1));
                    break;
                }
            }
        }
        return 0;
    }

    static class Pair {
        int location;
        int count;

        Pair(int location, int count) {
            this.location = location;
            this.count = count;
        }
    }
}
