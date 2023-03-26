package boj.`5000`

import java.util.StringTokenizer
import kotlin.collections.ArrayDeque

/*
https://www.acmicpc.net/problem/5430
5430.AC
풀이1.848ms
*/
fun main() {

    repeat(readln().toInt()) {
        val commands = readln().toCharArray()
        val n = readln().toInt()
        var numbers = readln()
        var reversed = false
        var isValid = true
        val deque = ArrayDeque<String>()

        if (n > 0) {
            val stringTokenizer = StringTokenizer(numbers.substring(1, numbers.length - 1), ",")
            while (stringTokenizer.hasMoreTokens()) {
                deque.addLast(stringTokenizer.nextToken())
            }
        }

        for (command in commands) {
            when (command) {
                'R' -> reversed = !reversed
                'D' -> {
                    if (deque.isEmpty()) {
                        isValid = false
                        break
                    }
                    if (!reversed) deque.removeFirst() else deque.removeLast()
                }
            }
        }

        if (isValid) {
            if (reversed)
                deque.reverse()
            println(deque.joinToString(",", "[", "]"))
        } else {
            println("error")
        }

    }

}
