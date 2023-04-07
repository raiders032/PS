package boj.`20000`

/**
 * https://www.acmicpc.net/problem/20040
 * 20040.사이클 게임
 * 풀이1.1020ms
 */
fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val disjointSet = IntArray(n) { i -> i }
    val graph = Array(n) { mutableListOf<Int>() }

    fun find(vertex: Int): Int {
        if (disjointSet[vertex] != vertex)
            disjointSet[vertex] = find(disjointSet[vertex])

        return disjointSet[vertex]
    }

    fun union(vertex1: Int, vertex2: Int): Boolean {
        val root1 = find(vertex1)
        val root2 = find(vertex2)

        if (root1 == root2)
            return false

        if (root1 < root2) {
            disjointSet[root2] = root1
        } else {
            disjointSet[root1] = root2
        }

        return true
    }

    var answer = 0

    for (i in 1..m){
        val (v1, v2) = readln().split(" ").map { it.toInt() }
        graph[v1].add(v2)
        graph[v2].add(v1)
        if (!union(v1, v2)) {
            answer = i
            break
        }
    }

    println(answer)
}