package boj.p11000;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/*
https://www.acmicpc.net/problem/11000
11000.강의실 배정
골드5
풀이1.812ms
 */

public class P11000 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] lectures = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer tokenizer = new StringTokenizer(br.readLine());

            int startTime = Integer.parseInt(tokenizer.nextToken());
            int endTime = Integer.parseInt(tokenizer.nextToken());

            lectures[i][0] = startTime;
            lectures[i][1] = endTime;
        }

        Arrays.sort(lectures, Comparator.comparingInt(l -> l[0]));

        PriorityQueue<Integer> endTimes = new PriorityQueue<>();
        endTimes.add(lectures[0][1]);

        for (int i = 1; i < n; i++) {
            if (lectures[i][0] < endTimes.peek()) {
                endTimes.add(lectures[i][1]);
                continue;
            }
            endTimes.poll();
            endTimes.add(lectures[i][1]);
        }

        System.out.println(endTimes.size());
    }
}
