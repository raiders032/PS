package boj.`10000`

import java.lang.StringBuilder
import java.util.StringTokenizer

/**
 * https://www.acmicpc.net/problem/10942
 * 10942.팰린드롬?
 * 풀이1.1128ms
 */
fun main() {
    val n = readln().toInt()
    var stringTokenizer = StringTokenizer(readln())
    val numbers = IntArray(n) { 0 }
    val cache = Array(n) { IntArray(n) { -1 } }
    repeat(n) {
        cache[it][it] = 1
    }

    fun dp(start: Int, end: Int): Int {
        if (end <= start) {
            return 1
        }

        if (cache[start][end] != -1)
            return cache[start][end]

        if (numbers[start] != numbers[end]) {
            cache[start][end] = 0
            return cache[start][end]
        }

        cache[start][end] = dp(start + 1, end - 1)
        return cache[start][end]
    }

    repeat(n) {
        numbers[it] = stringTokenizer.nextToken().toInt()
    }

    val m = readln().toInt()
    val answer = StringBuilder()
    repeat(m) {
        stringTokenizer = StringTokenizer(readln())
        val s = stringTokenizer.nextToken().toInt() - 1
        val e = stringTokenizer.nextToken().toInt() - 1

        answer.append(dp(s, e))
            .append("\n")
    }

    println(answer)
}