package boj.`7000`

/*
https://www.acmicpc.net/problem/7511
7511.소셜 네트워킹 어플리케이션
풀이1.1652ms
*/

var disjointSet: IntArray = IntArray(0)
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

fun main() {
    val answer = StringBuilder()

    repeat(readln().toInt()) { i ->
        val n = readln().toInt()
        disjointSet = IntArray(n + 1) { it }

        answer.append("Scenario ${i + 1}:\n")

        repeat(readln().toInt()) {
            val (a, b) = readln().split(" ").map { it.toInt() }
            union(a, b)
        }

        repeat(readln().toInt()) {
            val (a, b) = readln().split(" ").map { it.toInt() }
            if (find(a) == find(b))
                answer.append("1\n")
            else
                answer.append("0\n")
        }
        answer.append("\n")
    }

    println(answer)
}