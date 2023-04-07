package boj.p7000;
/*
https://www.acmicpc.net/problem/7785
7785.회사에 있는 사람
실버5
풀이1.1288ms
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P7785 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        TreeSet<String> workers = new TreeSet<>();

        while (n-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String enterOrLeave = st.nextToken();

            if (enterOrLeave.equals("enter")) {
                workers.add(name);
            } else {
                workers.remove(name);
            }
        }

        Iterator<String> iterator = workers.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
