package boj.`16000`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue
import java.util.StringTokenizer

/**
 * 16973.직사각형 탈출
 * https://www.acmicpc.net/problem/16973
 * 풀이1.2988ms
 */
fun main() {
    val bufferedReader = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = bufferedReader.readLine().split(" ").map { it.toInt() }
    val board = Array(n) { IntArray(m) }
    val visited = Array(n) { IntArray(m) { -1 } }

    fun validateArea(x: Int, y: Int, height: Int, width: Int): Boolean {
        for (i in x until x + height) {
            for (j in y until y + width) {
                if (i < 0 || i >= n || j < 0 || j >= m || board[i][j] == 1) {
                    return false
                }
            }
        }
        return true
    }

    fun visit(height: Int, width: Int, startX: Int, startY: Int, endX: Int, endY: Int) {
        val dx = arrayOf(-1, 0, 1, 0)
        val dy = arrayOf(0, 1, 0, -1)
        val queue: Queue<Pair<Int, Int>> = LinkedList()
        visited[startX][startY] = 0
        queue.add(Pair(startX, startY))

        while (queue.isNotEmpty()) {
            val (x, y) = queue.remove()

            if (x == endX && y == endY)
                return

            for (i in 0 until 4) {
                val nx = x + dx[i]
                val ny = y + dy[i]

                if (nx < 0 || nx >= n || ny < 0 || ny >= m || board[nx][ny] == 1 || visited[nx][ny] != -1)
                    continue

                if (!validateArea(nx, ny, height, width))
                    continue

                visited[nx][ny] = visited[x][y] + 1
                queue.add(Pair(nx, ny))
            }
        }
    }

    for (i in 0 until n) {
        var stringTokenizer = StringTokenizer(bufferedReader.readLine())
        for (j in 0 until m) {
            board[i][j] = stringTokenizer.nextToken().toInt()
        }

    }

    val command = bufferedReader.readLine().split(" ").map { it.toInt() - 1 }.toList()
    visit(command[0] + 1, command[1] + 1, command[2], command[3], command[4], command[5])
    println(visited[command[4]][command[5]])

}