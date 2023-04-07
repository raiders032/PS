package boj.`2000`

/*
https://www.acmicpc.net/problem/2168
2168.타일 위의 대각선
풀이.132ms
 */
fun main() {
    var (x, y) = readln().split(" ").map { it.toInt() }
    println(x + y - gcd(x, y))
}

fun gcd(a:Int, b:Int):Int {
    if (b == 0) {
        return a
    }

    return gcd(b, a % b)
}