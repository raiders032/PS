package boj.`14000`

import java.util.StringTokenizer

/*
https://www.acmicpc.net/problem/14719
14719.빗물
풀이1.140ms
 */
fun main() {
    val (h, w) = readln().split(" ").map { it.toInt() }
    val stringTokenizer = StringTokenizer(readln())
    val heights = mutableListOf<Int>()
    var maxNumberIndex = 0
    var maxNumber = 0
    var index = 0

    while (stringTokenizer.hasMoreTokens()) {
        val number = stringTokenizer.nextToken().toInt()
        heights.add(number)
        if (maxNumber < number) {
            maxNumber = number
            maxNumberIndex = index
        }
        index += 1
    }

    var answer = 0
    var right = 0
    var localMaxHeight = 0
    while (right < maxNumberIndex) {
        if (localMaxHeight < heights[right])
            localMaxHeight = heights[right]
        else
            answer += localMaxHeight - heights[right]

        right += 1
    }

    localMaxHeight = 0
    var left = w -1
    while (maxNumberIndex < left) {
        if (localMaxHeight < heights[left])
            localMaxHeight = heights[left]
        else
            answer += localMaxHeight - heights[left]
        left -= 1
    }

    println(answer)
}