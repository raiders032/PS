package boj.`11000`

import java.util.StringTokenizer

/**
 * https://www.acmicpc.net/problem/11657
 * 11657.타임머신
 * 풀이1.428ms
 */

data class Edge(val from: Int, val to: Int, val cost: Int)

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val edges = mutableListOf<Edge>()
    val distance = LongArray(n + 1) { Long.MAX_VALUE }
    distance[1] = 0

    repeat(m) {
        val stringTokenizer = StringTokenizer(readln())
        edges.add(
            Edge(
                stringTokenizer.nextToken().toInt(),
                stringTokenizer.nextToken().toInt(),
                stringTokenizer.nextToken().toInt()
            )
        )
    }

    repeat(n - 1) {
        for (edge in edges) {
            if (distance[edge.from] == Long.MAX_VALUE)
                continue

            if (distance[edge.from] + edge.cost < distance[edge.to]) {
                distance[edge.to] = distance[edge.from] + edge.cost
            }
        }
    }

    var isCycle = false

    for (edge in edges) {
        if (distance[edge.from] == Long.MAX_VALUE)
            continue

        if (distance[edge.from] + edge.cost < distance[edge.to]) {
            isCycle = true
            break
        }
    }

    if (isCycle)
        print("-1")
    else
        print(distance
            .slice(2 until distance.size)
            .map { if (it == Long.MAX_VALUE) -1 else it }
            .joinToString("\n"))

}