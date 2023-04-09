package boj.`3000`

import java.util.StringTokenizer

/*
https://www.acmicpc.net/problem/3151
3151.합이 0
풀이1.5036ms
 */
fun main() {
    val n = readln().toInt()
    val numbers = mutableListOf<Int>()

    with(StringTokenizer(readln())) {
        while (hasMoreTokens())
            numbers.add(nextToken().toInt())
    }

    numbers.sort()
    var answer = 0L

    fun binarySearchUpperBound(low: Int, high: Int, number: Int): Int {
        var low = low
        var high = high

        while (low + 1 < high) {
            val mid = (low + high) / 2
            if (numbers[mid] <= number) {
                low = mid
            } else {
                high = mid
            }
        }

        return high
    }

    fun binarySearchLowerBound(low: Int, high: Int, number: Int): Int {
        var low = low
        var high = high

        while (low + 1 < high) {
            val mid = (low + high) / 2
            if (numbers[mid] < number) {
                low = mid
            } else {
                high = mid
            }
        }

        return high
    }

    for (i in 0 until n - 2) {
        for (j in i + 1 until n - 1) {
            val target = -(numbers[i] + numbers[j])
            val upperBound = binarySearchUpperBound(j, n, target)
            val lowerBound = binarySearchLowerBound(j, n, target)
            answer += upperBound - lowerBound
        }
    }

    println(answer)
}