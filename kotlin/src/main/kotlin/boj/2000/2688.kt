package boj.`2000`

/*
https://www.acmicpc.net/problem/2688
2688.줄어들지 않아
풀이1.124ms
 */
fun main() {
    val dp = Array(65) { LongArray(10) { 0 } }

    for (i in 0..9) {
        dp[1][i] = 1
    }

    for (i in 1..64) {
        dp[i][0] = 1
    }

    for (i in 2..64) {
        for (j in 1..9) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        }
    }

    val answer = StringBuilder()
    repeat(readln().toInt()) {
        val n = readln().toInt()
        answer.append(dp[n].sum()).append("\n")
    }

    print(answer)
}