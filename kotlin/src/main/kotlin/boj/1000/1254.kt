package boj.`1000`

/*
https://www.acmicpc.net/problem/1254
1254.팰린드롬 만들기
풀이1.176ms
 */
fun main() {
    val chars = readln().toCharArray()
    val size = chars.size
    var maxLength = 1

    for (i in 2..size) {
        if (chars.slice(size - i until size) == chars.slice(size - i until size).reversed()){
            maxLength = i
        }
    }

    println(size + (size - maxLength))

}