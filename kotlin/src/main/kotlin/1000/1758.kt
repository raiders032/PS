package `1000`

import java.io.BufferedReader
import java.io.InputStreamReader

/**
 * 1758.알바생 강호
 * https://www.acmicpc.net/problem/1758
 * 풀이1.264ms
 */
fun main() {
    val bufferedReader = BufferedReader(InputStreamReader(System.`in`))
    val n = bufferedReader.readLine().toInt()
    val numbers = ArrayList<Int>()
    var answer:Long = 0

    for (i in 1..n) {
        numbers.add(bufferedReader.readLine().toInt())
    }

    numbers.sortBy { -it }

    for (i in 0 until n) {
        val tip = numbers[i] - i
        if (tip <= 0)
            continue
        answer += tip
    }

    println(answer)

}

