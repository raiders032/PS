package programmers;

/*
https://programmers.co.kr/learn/courses/30/lessons/1829?language=java
카카오프렌즈 컬러링북
레벨2
풀이1
 */

import static java.lang.Math.max;

public class 카카오프렌즈_컬러링북 {

    public static void main(String[] args) {
        카카오프렌즈_컬러링북 temp = new 카카오프렌즈_컬러링북();
        Solution solution = temp.new Solution();

        int[][] picture = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
        int[] result = solution.solution(6, 4, picture);
        System.out.println(result[0] + ", " + result[1]);
    }

    class Solution {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int m;
        int n;
        boolean[][] visited;

        public int[] solution(int m, int n, int[][] picture) {
            this.m = m;
            this.n = n;
            visited = new boolean[m][n];

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (picture[i][j] == 0 || visited[i][j]) {
                        continue;
                    }
                    numberOfArea++;
                    maxSizeOfOneArea = max(maxSizeOfOneArea, visit(picture, i, j));

                }
            }

            int[] answer = new int[2];
            answer[0] = numberOfArea;
            answer[1] = maxSizeOfOneArea;
            return answer;
        }

        private int visit(int[][] picture, int x, int y) {
            int area = 1;
            visited[x][y] = true;
            int[] dx = {-1, 0, 1, 0};
            int[] dy = {0, 1, 0, -1};

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= m || ny < 0 || ny >= n)
                    continue;

                if (visited[nx][ny])
                    continue;

                if (picture[nx][ny] == 0 || picture[x][y] != picture[nx][ny])
                    continue;

                area += visit(picture, nx, ny);
            }

            return area;
        }
    }
}
