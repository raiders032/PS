package boj.`15000`

import java.lang.StringBuilder

/**
 * 15991.1, 2, 3 더하기 6
 * https://www.acmicpc.net/problem/15991
 * 풀이1.200ms
 */
fun main() {
    val dp = LongArray(100001) { 0 }
    dp[1] = 1
    dp[2] = 2
    dp[3] = 2
    dp[4] = 3
    dp[5] = 3
    dp[6] = 6

    for (i in 4..100000) {
        dp[i] = (dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1_000_000_009
    }

    val stringBuilder = StringBuilder()
    repeat(readln().toInt()) {
        stringBuilder
            .append(dp[readln().toInt()])
            .append("\n")
    }

    println(stringBuilder)
}