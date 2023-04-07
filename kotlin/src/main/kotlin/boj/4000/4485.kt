package boj.`4000`

import java.lang.StringBuilder
import java.util.PriorityQueue

/*
https://www.acmicpc.net/problem/4485
4485.녹색 옷 입은 애가 젤다지?
풀이1.320ms
 */

fun main() {
    val dx = intArrayOf(-1, 0, 1, 0)
    val dy = intArrayOf(0, 1, 0, -1)
    var number = 1
    val answer = StringBuilder()

    while (true) {
        val n = readln().toInt()
        if (n == 0) break
        val distance = Array(n) { mutableListOf<Int>() }
        repeat(n) { row ->
            distance[row].addAll(readln().split(" ").map { it.toInt() }.toList())
        }

        val minDistance = Array(n) { IntArray(n) { Int.MAX_VALUE } }
        val minHeap = PriorityQueue<Node>()

        minDistance[0][0] = distance[0][0]
        minHeap.add(Node(distance[0][0], 0, 0))

        while (minHeap.isNotEmpty()) {
            val (currentDistance, x, y) = minHeap.remove()

            if (minDistance[x][y] < currentDistance)
                continue

            for (i in 0 until 4) {
                val nx = x + dx[i]
                val ny = y + dy[i]

                if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                    continue

                if (currentDistance + distance[nx][ny] < minDistance[nx][ny]) {
                    minDistance[nx][ny] = currentDistance + distance[nx][ny]
                    minHeap.add(Node(currentDistance + distance[nx][ny], nx, ny))
                }
            }

        }

        answer.append("Problem ${number}: ${minDistance[n - 1][n - 1]}\n")
        number += 1
    }

    println(answer)
}

data class Node(
    val distance:Int,
    val x:Int,
    val y:Int
):Comparable<Node> {
    override fun compareTo(other: Node): Int {
        return distance.compareTo(other.distance)
    }
}