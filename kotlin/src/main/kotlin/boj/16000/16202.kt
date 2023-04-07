package boj.`16000`

/*
https://www.acmicpc.net/problem/16202
16202.MST 게임
풀이1.608ms
 */
fun main() {
    val (n, m, k) = readln().split(" ").map { it.toInt() }
    val edges = mutableListOf<Vertex>()
    var disjointSet = Array(n + 1) { it }
    val answer = StringBuilder()

    fun find(vertex: Int): Int {
        if (disjointSet[vertex] != vertex)
            disjointSet[vertex] = find(disjointSet[vertex])

        return disjointSet[vertex]
    }

    fun union(vertex1: Int, vertex2: Int) {
        val root1 = find(vertex1)
        val root2 = find(vertex2)

        if (root1 <= root2)
            disjointSet[root2] = root1
        else
            disjointSet[root1] = root2
    }

    repeat(m) { index ->
        val (vertex1, vertex2) = readln().split(" ").map { it.toInt() }
        edges.add(Vertex(vertex1, vertex2, index + 1))
    }

    edges.sort()
    var count = 0

    for (i in 0..m - (n - 1)) {
        if (count == k)
            break

        var edgeCount = 0
        var weightSum = 0
        disjointSet = Array(n + 1) { it }

        for (j in i until m) {
            if (find(edges[j].from) == find(edges[j].to))
                continue

            union(edges[j].from, edges[j].to)
            edgeCount += 1
            weightSum += edges[j].weight

        }

        if (edgeCount == n - 1) {
            answer.append(weightSum).append(" ")
            count += 1
        } else
            break
    }

    for (i in 0 until k - count)
        answer.append("0 ")

    println(answer)

}

data class Vertex(
    val from: Int,
    val to: Int,
    val weight: Int
) : Comparable<Vertex> {

    override fun compareTo(other: Vertex): Int {
        return weight.compareTo(other.weight)
    }

}