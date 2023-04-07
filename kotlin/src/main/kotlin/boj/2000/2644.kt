package boj.`2000`
/*
https://www.acmicpc.net/problem/2644
2644.촌수계산
풀이1.176ms
 */
fun main() {
    val n = readln().toInt()
    val (start, end) = readln().split(" ").map { it.toInt() }
    val graph = Array(n + 1) { mutableListOf<Int>() }

    repeat(readln().toInt()) {
        var (v1, v2) = readln().split(" ").map { it.toInt() }
        graph[v1].add(v2)
        graph[v2].add(v1)
    }

    var answer = -1
    val visited = IntArray(n + 1) { -1 }
    val queue = ArrayDeque<Int>()
    queue.add(start)
    visited[start] = 0

    while (queue.isNotEmpty()) {
        val vertex = queue.removeFirst()

        if (vertex == end) {
            answer = visited[vertex]
            break
        }

        for (nextVertex in graph[vertex]) {
            if (visited[nextVertex] >= 0)
                continue

            visited[nextVertex] = visited[vertex] + 1
            queue.add(nextVertex)

        }
    }

    println(answer)

}