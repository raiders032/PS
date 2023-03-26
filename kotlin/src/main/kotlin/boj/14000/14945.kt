package boj.`14000`

/*
https://www.acmicpc.net/problem/14945
14945.불장난
풀이1.132ms
 */

fun main() {
    val n = readln().toInt()
    val dp = Array(n + 1) { IntArray(n + 1) }
    dp[2][1] = 2

    for (i in 3..n) {
        for (j in 1 until i) {
            dp[i][j] = (dp[i - 1][j] * 2 + dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 10007
        }
    }

    println(dp[n].sum() % 10007)
}