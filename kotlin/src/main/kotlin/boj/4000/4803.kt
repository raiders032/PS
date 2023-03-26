package boj.`4000`

import java.lang.StringBuilder

/*
https://www.acmicpc.net/problem/4803
4803.트리
풀이1.612ms
*/
var disjointSet = IntArray(0)
fun main() {
    val answer = StringBuilder()
    var index = 1

    while (true) {
        val (n, m) = readln().split(" ").map { it.toInt() }

        if (n == 0 && m == 0)
            break

        disjointSet = IntArray(n + 1) { it }

        repeat(m) {
            val (v1, v2) = readln().split(" ").map { it.toInt() }
            union(v1, v2)
        }

        val set = HashSet<Int>()
        repeat(n) {
            set.add(find(it + 1))
        }

        set.remove(0)
        answer.append("Case ${index++}: ")

        when (set.size) {
            0 -> answer.append("No trees.")
            1 -> answer.append("There is one tree.")
            else -> answer.append("A forest of ${set.size} trees.")
        }
        answer.append("\n")

    }

    println(answer)
}

fun find(vertex: Int): Int {
    if (disjointSet[vertex] != vertex) {
        disjointSet[vertex] = find(disjointSet[vertex])
    }

    return disjointSet[vertex]
}

fun union(vertex1: Int, vertex2: Int) {
    val root1 = find(vertex1)
    val root2 = find(vertex2)

    when {
        root1 < root2 -> disjointSet[root2] = root1
        root1 > root2 -> disjointSet[root1] = root2
        else -> {
            disjointSet[root1] = 0
            disjointSet[root2] = 0
        }
    }

}