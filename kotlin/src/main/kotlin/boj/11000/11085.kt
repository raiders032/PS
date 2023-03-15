package boj.`11000`

import java.util.PriorityQueue

/*
https://www.acmicpc.net/problem/11085
11085.군사 이동
풀이1.508ms
 */

fun main() {
    val (p, w) = readln().split(" ").map { it.toInt() }
    val (c, v) = readln().split(" ").map { it.toInt() }
    val priorityQueue = PriorityQueue<Triple<Int, Int, Int>>(compareBy { -it.third })
    val disjointSet = Array(p) { it }

    fun find(vertex: Int): Int {
        if (disjointSet[vertex] != vertex) {
            disjointSet[vertex] = find(disjointSet[vertex])
        }

        return disjointSet[vertex]
    }

    fun union(vertex1: Int, vertex2: Int) {
        val root1 = find(vertex1)
        val root2 = find(vertex2)

        if (root1 <= root2) {
            disjointSet[root2] = root1
        } else {
            disjointSet[root1] = root2
        }
    }

    repeat(w) {
        val (v1, v2, weight) = readln().split(" ").map { it.toInt() }
        priorityQueue.add(Triple(v1, v2, weight))
    }

    while (priorityQueue.isNotEmpty()) {
        val (v1, v2, weight) = priorityQueue.remove()
        union(v1, v2)
        if (find(c) == find(v)) {
            println(weight)
            break
        }
    }

}