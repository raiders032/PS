package boj.`7000`

import java.lang.StringBuilder

/*
7795.먹을 것인가 먹힐 것인가
https://www.acmicpc.net/problem/7795
풀이1.696ms
*/
fun main() {
    val answer = StringBuilder("")

    repeat(readln().toInt()) {
        var count = 0
        val N = readln()
        val A = readln().split(" ").map { it.toInt() }.toList()
        val B = readln().split(" ").map { it.toInt() }.toList().sorted()

        repeat(A.size) {
            count += biSearch(B, A[it])
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