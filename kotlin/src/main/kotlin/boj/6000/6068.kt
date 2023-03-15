package boj.`6000`

import java.util.PriorityQueue
import kotlin.math.min

/*
https://www.acmicpc.net/problem/6068
6068.시간 관리하기
풀이.208ms
 */
data class Job(val time: Int, val end: Int) : Comparable<Job> {
    override fun compareTo(other: Job) = compareValuesBy(this, other,
        { it.time },
        { it.end }
    )

}

fun main() {
    val n = readln().toInt()
    val priorityQueue = PriorityQueue<Job>()
    var answer = Int.MAX_VALUE

    repeat(n) {
        val (time, end) = readln().split(" ").map { it.toInt() }
        priorityQueue.add(Job(end, time))
    }

    var currentEnd = 0
    while (true) {
        val (end, time) = priorityQueue.remove()
        currentEnd += time

        if (currentEnd > end) {
            println(-1)
            break
        }

        answer = min(answer, end - currentEnd)

        if (priorityQueue.isEmpty()) {
            println(answer)
            break
        }
    }

}

/*
4
17 63
32 95
38 129
11 104
31
---

 */