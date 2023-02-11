package boj.`13000`

/*
https://www.acmicpc.net/problem/13913
13913.숨바꼭질 4
풀이1.460ms
 */
fun main() {
    val (n, k) = readln().split(" ").map { it.toInt() }
    val visited = IntArray(100001) { -2 }
    val queue = ArrayDeque<Int>()

    visited[n] = -1
    queue.addLast(n)

    while (queue.isNotEmpty()) {
        val x = queue.removeFirst()

        if (x == k) {
            val answer = mutableListOf(k)
            var currentNode = k
            while (visited[currentNode] != -1) {
                answer.add(visited[currentNode])
                currentNode = visited[currentNode]
            }
            answer.reverse()
            println(answer.size - 1)
            println(answer.joinToString(" "))
            break
        }

        for (dx in listOf(-1, 1, x)) {
            val nx = x + dx

            if (nx < 0 || nx > 100000)
                continue

            if (visited[nx] != -2)
                continue

            visited[nx] = x
            queue.addLast(nx)
        }
    }
}