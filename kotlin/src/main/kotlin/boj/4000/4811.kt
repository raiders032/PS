package boj.`4000`

/*
https://www.acmicpc.net/problem/4811
4811.알약
풀이1.104ms
*/
fun main() {
    val dp = Array(31) { LongArray(31) { 1 } }

    for (i in 1..30) {
        for (j in 0..30 - i) {
            if (j == 0)
                dp[i][j] = dp[i - 1][j + 1]
            else
                dp[i][j] = dp[i - 1][j + 1] + dp[i][j - 1]
        }
    }

    val answer = StringBuilder()
    while (true) {
        val n = readln().toInt()
        if (n == 0)
            break

        answer.append(dp[n][0])
            .append("\n")
    }
    println(answer)
}