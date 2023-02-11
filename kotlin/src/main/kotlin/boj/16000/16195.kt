package boj.`16000`

/*
https://www.acmicpc.net/problem/16195
16195.1, 2, 3 더하기 9
풀이1.280ms
 */
fun main() {
    val dp = Array(1001) { LongArray(1001) { 0 } }

    for (i in 1..1000) {
        dp[i][i] = 1
    }

    dp[2][1] = 1
    dp[3][1] = 1

    for (i in 3..1000) {
        for (j in 2 until i) {
            dp[i][j] += dp[i - 1][j - 1] % 1000000009
            dp[i][j] += dp[i - 2][j - 1] % 1000000009
            dp[i][j] += dp[i - 3][j - 1] % 1000000009
            dp[i][j] = dp[i][j] % 1000000009
        }
    }

    val answer = StringBuilder()
    repeat(readln().toInt()) {
        val (n, m) = readln().split(" ").map { it.toInt() }
        var sum = 0L
        for (i in 1..m) {
            sum += dp[n][i] % 1000000009
        }
        answer.append(sum % 1000000009).append("\n")
    }

    print(answer)
}