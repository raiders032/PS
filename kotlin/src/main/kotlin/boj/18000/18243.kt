package boj.`18000`

import kotlin.system.exitProcess

/**
 * 18243.Small World Network
 * https://www.acmicpc.net/problem/18243
 * 풀이1.284ms
 */
fun main() {
    val (n, k) = readln().split(" ").map { it.toInt() }
    val dist = Array(n) { LongArray(n) { Long.MAX_VALUE } }

    repeat(k) {
        val (vertex1, vertex2) = readln().split(" ").map { it.toInt() - 1 }
        dist[vertex1][vertex2] = 1
        dist[vertex2][vertex1] = 1
    }

    repeat(n) {
        dist[it][it] = 0
    }

    for (i in 0 until n) {
        for (j in 0 until n) {
            for (k in 0 until n) {
                if (dist[j][i] < dist[j][k] - dist[i][k])
                    dist[j][k] = dist[j][i] + dist[i][k]
            }
        }
    }

    for (i in 0 until n) {
        for (j in 0 until n) {
            if (dist[i][j] > 6) {
                println("Big World!")
                exitProcess(0)
            }
        }
    }

    println("Small World!")

}