package boj.`13000`

import java.util.StringTokenizer
import kotlin.math.max
/*
https://www.acmicpc.net/problem/13398
13398.연속합 2
풀이1.412ms
 */
fun main() {
    val n = readln().toInt()
    val stringTokenizer = StringTokenizer(readln())
    val numbers = mutableListOf<Int>()
    val dp = Array(n) { IntArray(2) { 0 } }


    while (stringTokenizer.hasMoreTokens()) {
        numbers.add(stringTokenizer.nextToken().toInt())
    }

    dp[0][0] = numbers[0]
    var answer = numbers[0]
    for (i in 1 until n) {
        dp[i][0] = max(dp[i - 1][0] + numbers[i], numbers[i])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + numbers[i])
        answer = max(answer, dp[i].max())
    }

    println(answer)
}