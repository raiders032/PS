/*
https://www.acmicpc.net/problem/6603
6603.로또
실버1
백트래킹,조합론,수학,재귀
풀이1. 348ms
 */
package boj.p6000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P6603 {

    static void solve(List<Integer> numbers, int index, List<Integer> selected_numbers){
        if (selected_numbers.size() == 6){
            for (Integer number : selected_numbers) {
                System.out.print(number + " ");
            }
            System.out.println();
            return;
        }

        for (int i = index; i < numbers.size(); i++) {
            selected_numbers.add(numbers.get(i));
            solve(numbers, i + 1, selected_numbers);
            selected_numbers.remove(selected_numbers.size() - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            if (k == 0)
                break;
            List<Integer> numbers = new ArrayList<>();
            for (int i = 0; i < k; i++) {
                numbers.add(Integer.parseInt(st.nextToken()));
            }
            solve(numbers, 0, new ArrayList<>());
            System.out.println();
        }
    }
}
