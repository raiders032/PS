package boj.`21000`

import java.util.StringTokenizer

/*
https://www.acmicpc.net/problem/21925
21925.짝수 팰린드롬
풀이1.344ms
 */

fun main() {
    val n = readln().toInt()
    val stringTokenizer = StringTokenizer(readln())
    val numbers = mutableListOf<Int>()
    while (stringTokenizer.hasMoreTokens()) {
        numbers.add(stringTokenizer.nextToken().toInt())
    }

    var left = 0
    var right = 1
    var count = 0

    while (right < n) {
        if (numbers.slice(left..right) == numbers.slice(left..right).reversed()) {
            count += 1
            left = right + 1
            right = left + 1
            continue
        }

        right += 2

        if (right >= n) {
            count = -1
            break
        }
    }

    print(count)
}