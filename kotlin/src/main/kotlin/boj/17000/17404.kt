package boj.`17000`

import kotlin.math.min
/*
https://www.acmicpc.net/problem/17404
17404.RGB거리 2
풀이1.228ms
 */
fun main() {
    val n = readln().toInt()
    val board = Array(n) { mutableListOf<Int>() }

    repeat(n) {
        board[it].addAll(readln().split(" ").map { it.toInt() }.toMutableList())
    }

    val dp = Array(n) { Array(3) { IntArray(3) { 10000000 } } }
    dp[0][0][0] = board[0][0]
    dp[0][1][1] = board[0][1]
    dp[0][2][2] = board[0][2]

    for (i in 1 until n - 1) {
        for (j in 0 until 3) {
            for (k in 0 until 3) {
                if (dp[i - 1][(j + 1) % 3][k] != 10000000)
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][(j + 1) % 3][k] + board[i][j])

                if (dp[i - 1][(j + 2) % 3][k] != 10000000)
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][(j + 2) % 3][k] + board[i][j])
            }
        }
    }

    for (j in 0 until 3) {
        for (k in 0 until 3) {
            if (j == k)
                continue
            dp[n - 1][j][k] = min(dp[n - 1][j][k], dp[n - 2][(j + 1) % 3][k] + board[n - 1][j])
            dp[n - 1][j][k] = min(dp[n - 1][j][k], dp[n - 2][(j + 2) % 3][k] + board[n - 1][j])
        }
    }

    println(dp[n-1].minBy { it.min() }.min())

}