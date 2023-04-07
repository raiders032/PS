package boj.`2000`

/*
https://www.acmicpc.net/problem/2553
2553.마지막 팩토리얼 수
풀이1.
 */
fun main() {
    val n = readln().toInt()
    var result:Long = 1

    for (i in 1..n) {
        result *= i
        result %= 10000000
        while (result % 10 == 0L) {
            result /= 10
        }
    }

    println(result % 10)

}
