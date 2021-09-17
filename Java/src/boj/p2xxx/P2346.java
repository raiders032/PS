package boj.p2xxx;
/*
https://www.acmicpc.net/problem/2346
2346.풍선 터뜨리기
실버3
풀이1.200ms
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class P2346 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Deque<int[]> balloons = new ArrayDeque<>();
        StringBuilder answer = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int countTokens = st.countTokens();
        for (int i = 1; i <= countTokens; i++) {
            balloons.add(new int[] {i, Integer.parseInt(st.nextToken())} );
        }

        while (!balloons.isEmpty()) {
            int[] balloon = balloons.pollFirst();
            answer.append(balloon[0]).append(" ");
            if (balloons.isEmpty())
                break;
            if (balloon[1] > 0) {
                for (int i = 0; i < balloon[1] - 1; i++) {
                    balloons.addLast(balloons.pollFirst());
                }
            } else {
                for (int i = 0; i < -balloon[1]; i++) {
                    balloons.addFirst(balloons.pollLast());
                }
            }
        }
        System.out.println(answer);
    }
}
