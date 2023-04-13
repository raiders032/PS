package boj.`1000`

import java.lang.StringBuilder

/*
https://www.acmicpc.net/problem/1012
1012.유기농 배추
풀이1.268ms
 */

fun main() {
    val answer = StringBuilder()
    var visited = Array(0) { BooleanArray(0) { false } }
    var board = Array(0) { IntArray(0) { 0 } }
    val dx = intArrayOf(-1, 0, 1, 0)
    val dy = intArrayOf(0, 1, 0, -1)

    fun visit(n: Int, m: Int, x: Int, y: Int) {
        val queue = ArrayDeque<Pair<Int, Int>>()
        visited[x][y] = true
        queue.add(Pair(x, y))

        while (queue.isNotEmpty()) {
            val (x, y) = queue.removeFirst()
            for (i in 0 until 4) {
                val nx = x + dx[i]
                val ny = y + dy[i]

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue

                if (visited[nx][ny] || board[nx][ny] == 0)
                    continue

                visited[nx][ny] = true
                queue.add(Pair(nx, ny))
            }
        }
    }

    repeat(readln().toInt()) {
        val (m, n, k) = readln().split(" ").map { it.toInt() }
        var count = 0

        board = Array(n) { IntArray(m) { 0 } }
        repeat(k) {
            val (y, x) = readln().split(" ").map { it.toInt() }
            board[x][y] = 1
        }

        visited = Array(n) { BooleanArray(m) { false } }

        for (x in 0 until n) {
            for (y in 0 until m) {
                if (board[x][y] == 0 || visited[x][y])
                    continue
                visit(n, m, x, y)
                count += 1
            }
        }

        answer.append(count).append("\n")

    }

    println(answer)
}