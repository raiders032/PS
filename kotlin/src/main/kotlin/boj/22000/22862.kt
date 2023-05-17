package boj.`22000`

import java.lang.Math.max
import java.util.StringTokenizer

/*
https://www.acmicpc.net/problem/22862
22862.가장 긴 짝수 연속한 부분 수열 (large)
풀이1.676ms
 */
fun main() {
    val (n, k) = readln().split(" ").map { it.toInt() }
    val numbers = IntArray(n)

    with(StringTokenizer(readln())) {
        repeat(n) { i ->
            numbers[i] = nextToken().toInt()
        }
    }

    var low = 0
    var high = 0
    var evenCount = if (numbers[0] % 2 == 0) 1 else 0
    var oddCount = if (numbers[0] % 2 == 0) 0 else 1
    var answer = if (numbers[0] % 2 == 0) 1 else 0

    while (high < n - 1) {
        if (oddCount <= k) {
            high++
            if (numbers[high] % 2 == 0)
                evenCount++
            else
                oddCount++
        } else {
            if (numbers[low] % 2 == 0)
                evenCount--
            else
                oddCount--
            low++
        }

        if (oddCount <= k)
            answer = max(answer, evenCount)

    }

    println(answer)
}