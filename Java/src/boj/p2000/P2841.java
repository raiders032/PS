package boj.p2000;
/*
https://www.acmicpc.net/problem/2841
2841.외계인의 기타 연주
실버1
풀이1.892ms
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class P2841 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        List<Stack<Integer>> lines = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            lines.add(new Stack<Integer>());
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            int fret = Integer.parseInt(st.nextToken());

            if (lines.get(number).empty()) {
                lines.get(number).push(fret);
                count += 1;
            } else if (lines.get(number).peek() < fret) {
                lines.get(number).push(fret);
                count += 1;
            } else if (lines.get(number).peek() > fret) {
                while (!lines.get(number).empty() && lines.get(number).peek() > fret) {
                    lines.get(number).pop();
                    count += 1;
                }
                if (lines.get(number).empty() || lines.get(number).peek() != fret) {
                    lines.get(number).push(fret);
                    count += 1;
                }
            }
        }
        System.out.println(count);
    }
}

/*
4 10
1 1
1 2
1 3
1 1
5
---
3 15
1 5
1 10
1 5
3
---
 */