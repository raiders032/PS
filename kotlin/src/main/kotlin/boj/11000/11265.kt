package boj.`11000`

import java.util.StringTokenizer

/**
 * https://www.acmicpc.net/problem/11265
 * 11265.끝나지 않는 파티
 * 풀이1.824ms
 */
fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val distance = Array(n) { mutableListOf<Long>() }

    repeat(n) {
        val stringTokenizer = StringTokenizer(readln())
        while (stringTokenizer.hasMoreTokens())
            distance[it].add(stringTokenizer.nextToken().toLong())
    }

    for (i in 0 until n) {
        for (j in 0 until n) {
            for (k in 0 until n) {
                if (distance[j][k] > distance[j][i] + distance[i][k])
                    distance[j][k] = distance[j][i] + distance[i][k]
            }
        }
    }

    val answer = StringBuilder()

    repeat(m) {
        val stringTokenizer = StringTokenizer(readln())
        val start = stringTokenizer.nextToken().toInt() - 1
        val end = stringTokenizer.nextToken().toInt() - 1
        val dist = stringTokenizer.nextToken().toInt()

        if (distance[start][end] <= dist)
            answer.append("Enjoy other party\n")
        else
            answer.append("Stay here\n")
    }

    print(answer)

}