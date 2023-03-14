package boj.`14000`

/*
https://www.acmicpc.net/problem/14888
14888.연산자 끼워넣기
풀이1.180ms
*/
fun main() {
    val n = readln().toInt()
    val numbers = readln().split(" ").map { it.toLong() }.toList()
    val operatorCount = readln().split(" ").map { it.toInt() }.toMutableList()
    var maxAnswer = Long.MIN_VALUE
    var minAnswer = Long.MAX_VALUE

    fun dfs(level: Int, result: Long) {
        if (level == n - 1) {
            maxAnswer = maxOf(maxAnswer, result)
            minAnswer = minOf(minAnswer, result)
            return
        }

        for (i in 0 until 4) {
            if (operatorCount[i] > 0) {
                operatorCount[i]--
                when (i) {
                    0 -> dfs(level + 1, result + numbers[level + 1])
                    1 -> dfs(level + 1, result - numbers[level + 1])
                    2 -> dfs(level + 1, result * numbers[level + 1])
                    3 -> dfs(level + 1, result / numbers[level + 1])
                }
                operatorCount[i]++
            }
        }
    }

    dfs(0, numbers[0])
    println(maxAnswer)
    println(minAnswer)
}