/*
https://www.acmicpc.net/problem/1339
1339.단어 수학
골드4
브루트포스,그리디알고리즘
풀이1.224ms
 */

package boj.p1000;

import java.util.*;

public class P1339 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<Character, Integer> charScoreMap = new HashMap<>();
        int n = scanner.nextInt();
        char[][] board = new char[n][10];
        for (int i = 0; i < n; i++) {
            board[i] = scanner.next().toCharArray();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < board[i].length; j++) {
                int score = (int) Math.pow(10, board[i].length - j - 1);
                char key = board[i][j];
                if (charScoreMap.containsKey(key)){
                    Integer value = charScoreMap.get(key);
                    charScoreMap.put(key, value +  score);
                }
                else{
                    charScoreMap.put(key, score);
                }
            }
        }

        List<Map.Entry<Character, Integer>> entries = new ArrayList<>(charScoreMap.entrySet());
        Collections.sort(entries, new Comparator<Map.Entry<Character, Integer>>() {
            @Override
            public int compare(Map.Entry<Character, Integer> o1, Map.Entry<Character, Integer> o2) {
                return o2.getValue() - o1.getValue();
            }
        });

        int res = 0;
        for (int i = 0; i < entries.size(); i++) {
            res += (9 - i ) * entries.get(i).getValue();
        }

        System.out.println(res);
    }

}
