package boj.`11000`

import java.util.*

/*
https://www.acmicpc.net/problem/11725
11725.트리의 부모 찾기
풀이1.1336ms
*/
fun main() {
    val n = readln().toInt()
    val graph = Array(n + 1) { mutableListOf<Int>() }
    val tree = IntArray(n + 1) { 1 }
    val visited = BooleanArray(n + 1) { false }

    fun visit(root: Int) {
        val queue: Queue<Int> = ArrayDeque()
        queue.add(root)

        while (queue.isNotEmpty()) {
            val parent = queue.remove()
            if (visited[parent])
                continue
            visited[parent] = true

            graph[parent]
                .stream()
                .filter { !visited[it] }
                .forEach { child ->
                    queue.add(child)
                    tree[child] = parent
                }
        }
    }

    repeat(n - 1) {
        val stringTokenizer = StringTokenizer(readln())
        val v1 = stringTokenizer.nextToken().toInt()
        val v2 = stringTokenizer.nextToken().toInt()
        graph[v1].add(v2)
        graph[v2].add(v1)
    }

    visit(1)
    val answer = tree.slice(2 until tree.size)
        .joinToString("\n")
    println(answer)

}

