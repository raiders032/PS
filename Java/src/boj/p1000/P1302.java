package boj.p1000;
/*
https://www.acmicpc.net/problem/1302
1302.베스트셀러
실버4
풀이1.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class P1302 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> book_count = new HashMap<>();

        while (n-- > 0) {
            String name = br.readLine();
            if (book_count.containsKey(name)) {
                book_count.put(name, book_count.get(name) + 1);
            } else {
                book_count.put(name, 1);
            }
        }

        Map.Entry<String, Integer> max_book = book_count.entrySet().stream()
                .sorted(Collections.reverseOrder(Map.Entry.comparingByValue())).findFirst().get();
        System.out.println(max_book.getKey());
    }
}
