package boj.p11000;

/**
 * https://www.acmicpc.net/problem/11286
 * 11286.절댓값 힙
 * 풀이2
 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Queue;

public class P11286 {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bufferedReader.readLine());
        StringBuilder stringBuilder = new StringBuilder();

        Queue<Integer> heap = new PriorityQueue<>((num1, num2) -> {
            int num1Abs = Math.abs(num1);
            int num2Abs = Math.abs(num2);

            if (num1Abs < num2Abs) {
                return -1;
            } else if (num1Abs > num2Abs) {
                return 1;
            }

            if (num1 < num2) {
                return -1;
            } else if (num1 > num2) {
                return 1;
            }
            return 0;
        });

        for (int i = 0; i < n; i++) {
            int number = Integer.parseInt(bufferedReader.readLine());
            if (number == 0) {
                if (heap.size() == 0) {
                    stringBuilder.append("0").append("\n");
                    continue;
                }
                stringBuilder.append(heap.remove()).append("\n");
                continue;
            }
            heap.add(number);
        }

        System.out.println(stringBuilder);

    }
}
