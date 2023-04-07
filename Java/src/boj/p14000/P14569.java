package boj.p14000;
/*
https://www.acmicpc.net/problem/14569
14569.시간표 짜기
실버2
풀이1.792ms
 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P14569 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Set<Integer>> subjects = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            subjects.add(new HashSet<>());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int len = Integer.parseInt(st.nextToken());
            for (int j = 0; j < len; j++) {
                subjects.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }

        int m = Integer.parseInt(br.readLine());
        List<Set<Integer>> students = new ArrayList<>();
        int[] answer = new int[m];

        for (int i = 0; i < m; i++) {
            students.add(new HashSet<>());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int len = Integer.parseInt(st.nextToken());
            for (int j = 0; j < len; j++) {
                students.get(i).add(Integer.parseInt(st.nextToken()));
            }

            for (int j = 0; j < n; j++) {
                if (students.get(i).containsAll(subjects.get(j))) {
                    answer[i] += 1;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            System.out.println(answer[i]);
        }
    }
}
