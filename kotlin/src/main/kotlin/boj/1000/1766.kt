package boj.`1000`

import java.lang.StringBuilder
import java.util.PriorityQueue

/*
https://www.acmicpc.net/problem/1766
1766.문제집
풀이1.1348ms
 */
fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val inDegrees = IntArray(n + 1) { 0 }
    val graph = Array(n + 1) { mutableListOf<Int>() }
    val visited = mutableSetOf<Int>()
    val answer = StringBuilder()

    repeat(m) {
        val (v1, v2) = readln().split(" ").map { it.toInt() }
        inDegrees[v2] += 1
        graph[v1].add(v2)
    }

    val queue = PriorityQueue<Node>()

    for (i in 1..n) {
        queue.add(Node(inDegrees[i], i))
    }

    while (queue.isNotEmpty()) {
        val (indegree, vertex) = queue.remove()

        if (visited.contains(vertex))
            continue

        visited.add(vertex)
        answer.append(vertex).append(" ")

        for (nextVertex in graph[vertex]){
            inDegrees[nextVertex] -= 1
            queue.add(Node(inDegrees[nextVertex], nextVertex))
        }

    }

    println(answer)

}

data class Node(val inDegree: Int, val vertex: Int) : Comparable<Node> {
    override fun compareTo(other: Node) =
        compareValuesBy(this, other, Node::inDegree, Node::vertex)
}
