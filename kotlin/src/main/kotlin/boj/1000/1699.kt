package boj.`1000`

import kotlin.math.min
import kotlin.math.pow
import kotlin.math.sqrt

/*
https://www.acmicpc.net/problem/1699
1699.제곱수의 합
풀이1.172ms
 */
fun main() {
    val target = readln().toInt()
    val dp = IntArray(100001) { Int.MAX_VALUE }
    dp[0] = 0
    dp[1] = 1

    for (i in 1..100000) {
        for (j in sqrt(i.toDouble()).toInt().toDouble().toInt() downTo 1){
            dp[i] = min(dp[i], dp[i - j.toDouble().pow(2).toInt()] + 1)
        }

    }
    println(dp[target])
}