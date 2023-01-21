package boj.`14000`

import java.lang.StringBuilder

/**
 * https://www.acmicpc.net/problem/14675
 * 14675.단절점과 단절선
 * 풀이1.748ms
 */
fun main() {
    val n = readln().toInt()
    val degree = IntArray(n + 1) { 0 }

    repeat(n - 1){
        val (parent, child) = readln().split(" ").map { it.toInt() }
        degree[parent] += 1
        degree[child] += 1
    }

    val q = readln().toInt()
    val answer = StringBuilder()
    repeat(q) {
        val (t, k) = readln().split(" ").map { it.toInt() }
        if (t == 1)
            answer.append(if (degree[k] == 1 ) "no" else "yes")
        else
            answer.append("yes")
        answer.append("\n")
    }
    println(answer)

}