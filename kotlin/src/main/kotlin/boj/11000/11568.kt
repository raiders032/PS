package boj.`11000`

import kotlin.math.max

/**
 * https://www.acmicpc.net/problem/11568
 * 11568.민균이의 계략
 * 풀이1.268ms
 */
fun main() {
    val n = readln().toInt()
    val numbers = readln().split(" ").map { it.toInt() }.toList()
    val dp = IntArray(n) { 1 }

    for (i in 0 until n) {
        for (j in 0 until i) {
            if (numbers[j] < numbers[i])
                dp[i] = max(dp[i], dp[j] + 1)
        }
    }

    println(dp.max())

}