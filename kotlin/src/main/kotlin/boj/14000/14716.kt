package boj.`14000`

/**
 * 14716.현수막
 * https://www.acmicpc.net/problem/14716
 * 풀이1.384ms
 */
fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val board = ArrayList<ArrayList<Int>>(n)
    val visited = Array(n) { Array(m) { false } }
    val dx = arrayOf(-1, -1, 0, 1, 1, 1, 0, -1)
    val dy = arrayOf(0, 1, 1, 1, 0, -1, -1, -1)

    fun visit(x: Int, y: Int) {
        visited[x][y] = true

        for (i in 0 until  8) {
            val nx = x + dx[i]
            val ny = y + dy[i]

            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue

            if (visited[nx][ny] || board[nx][ny] == 0)
                continue

            visit(nx, ny)
        }
    }

    repeat(n) {
        board.add(readln().split(" ").map { it.toInt() }.toList() as ArrayList<Int>)
    }

    var count = 0

    for (x in 0 until n) {
        for (y in 0 until m) {
            if (visited[x][y] || board[x][y] == 0)
                continue
            count += 1
            visit(x, y)
        }
    }

    println(count)

}

