package boj.`1000`

import java.util.PriorityQueue
import kotlin.system.exitProcess

/*
https://www.acmicpc.net/problem/1655
1655.가운데를 말해요
풀이1.472ms
 */
fun main() {
    val n = readln().toInt()
    val left = PriorityQueue<Int>(reverseOrder())
    val right = PriorityQueue<Int>()
    val answer = StringBuilder()
    val first = readln().toInt()

    if (n == 1) {
        println(first)
        exitProcess(0)
    }

    val second = readln().toInt()

    if (first <= second) {
        left.add(first)
        right.add(second)
    } else {
        left.add(second)
        right.add(first)
    }

    answer.append(first).append("\n")
    answer.append(left.element()).append("\n")

    repeat(n - 2) {
        val number = readln().toInt()

        if (right.element() < number) {
            right.add(number)
        } else {
            left.add(number)
        }

        if (right.size + 1 < left.size) {
            right.add(left.remove())
        }

        if (left.size < right.size) {
            left.add(right.remove())
        }

        answer.append(left.element()).append("\n")
    }

    println(answer)

}