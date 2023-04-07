package boj.`14000`

import kotlin.math.max

/*
https://www.acmicpc.net/problem/14728
14728.벼락치기
풀이1.232ms
 */

fun main() {
    val (n, t) = readln().split(" ").map { it.toInt() }
    val chapters = mutableListOf(Pair(0, 0))

    repeat(n) {
        val (k, s) = readln().split(" ").map { it.toInt() }
        chapters.add(Pair(k, s))
    }

    val dp = Array(n + 1) { IntArray(t + 1) { 0 } }

    for (i in 1..n) {
        for (j in 1..t) {
            dp[i][j] = dp[i - 1][j]
            if (chapters[i].first <= j)
                dp[i][j] = max(dp[i][j], dp[i - 1][j - chapters[i].first] + chapters[i].second)
        }
    }

    println(dp[n][t])
}