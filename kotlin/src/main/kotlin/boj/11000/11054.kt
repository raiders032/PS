package boj.`11000`

import java.lang.Integer.max

fun main() {
    val n = readln().toInt()
    val numbers = readln().split(" ").map { it.toInt() }.toList()
    val dp = Array(n) { IntArray(2) { 1 } }

    for (i in 0 until n) {
        for (j in 0 until i) {
            if (numbers[j] < numbers[i])
                dp[i][0] = max(dp[i][0], dp[j][0] + 1)
            if (numbers[n - i - 1] > numbers[n - j - 1])
                dp[n - i - 1][1] = max(dp[n - i - 1][1], dp[n - j - 1][1] + 1)
        }
    }

    println(dp.maxOf { it.sum() } - 1)
}