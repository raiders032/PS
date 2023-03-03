package boj.`13000`

import kotlin.system.exitProcess

/*
https://www.acmicpc.net/problem/13019
13019.A를 B로
풀이1.172ms
 */

fun main() {
    var answer = 0
    val a = readln()
    val b = readln()
    var pointA = a.length - 1
    var pointB = b.length - 1

    if (a.toList().sorted() != b.toList().sorted()) {
        println(-1)
        exitProcess(0)
    }

    while (pointA >= 0) {
        if (a[pointA] == b[pointB]) {
            pointA -= 1
            pointB -= 1
        } else {
            pointA -= 1
            answer += 1
        }
    }

    print(answer)
}
