package boj.`16000`


/**
 * https://www.acmicpc.net/problem/16948
 * 16948.데스 나이트
 * 풀이1.212ms
 */
fun main() {
    val n = readln().toInt()
    val (x1, y1, x2, y2) = readln().split(" ").map { it.toInt()}
    val visited = Array(n) { (BooleanArray(n) { false }) }
    val queue = ArrayDeque<Point>()
    var answer = -1
    val dx = arrayOf(-2, -2, 0, 0, 2, 2)
    val dy = arrayOf(-1, 1, -2, 2, -1, 1)

    visited[x1][y1] = true
    queue.add(Point(x1, y1, 0))

    while (!queue.isEmpty()) {
        val currentPoint = queue.removeFirst()

        if (x2 == currentPoint.x && y2 == currentPoint.y) {
            answer = currentPoint.distance
            break
        }

        for (i in 0 until 6) {
            val nx = currentPoint.x + dx[i]
            val ny = currentPoint.y + dy[i]

            if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny])
                continue

            visited[nx][ny] = true
            queue.addLast(Point(nx, ny, currentPoint.distance + 1))

        }
    }

    println(answer)

}

data class Point(val x: Int, val y: Int, val distance: Int)