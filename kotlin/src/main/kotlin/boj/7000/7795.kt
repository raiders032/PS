package boj.`7000`

import java.lang.StringBuilder

/**
 * 7795.먹을 것인가 먹힐 것인가
 * https://www.acmicpc.net/problem/7795
 * 풀이1.708ms
 */
fun main() {
    val n = readln().toInt()
    val answer = StringBuilder("")

    repeat(n) {
        var count = 0
        val N = readln()
        val A = readln().split(" ").map { it.toInt() }.toList()
        val B = readln().split(" ").map { it.toInt() }.toList().sorted()

        for (i in 0 until A.size) {
            count += biSearch(B, A[i])
        }
        answer
            .append(count)
            .append("\n")
    }

    println(answer)
}

fun biSearch(array: List<Int>, target: Int): Int {
    var low = -1
    var high = array.size

    while (low + 1 < high) {
        val mid = (low + high) / 2

        if (array[mid] >= target)
            high = mid
        else
            low = mid
    }

    return high
}