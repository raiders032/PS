package boj.`17000`

/*
https://www.acmicpc.net/problem/17123
17123.배열 놀이
풀이1.4280ms
 */

fun main() {
    val answer = StringBuilder()

    repeat(readln().toInt()) {
        val (n, m) = readln().split(" ").map { it.toInt() }
        val board = mutableListOf<MutableList<Int>>()
        val rowSum = IntArray(n) { 0 }
        val colSum = IntArray(n) { 0 }

        repeat(n) {
            board.add(readln().split(" ").map { it.toInt() }.toMutableList())
        }

        for (i in 0 until n) {
            for (j in 0 until n) {
                rowSum[i] += board[i][j]
                colSum[i] += board[j][i]
            }
        }

        repeat(m) {
            var (r1, c1, r2, c2, v) = readln().split(" ").map { it.toInt() - 1 }
            v += 1

            for (i in r1..r2) {
                rowSum[i] += (c2 - c1 + 1) * v
            }

            for (i in c1..c2) {
                colSum[i] += (r2 - r1 + 1) * v
            }
        }

        answer.append(rowSum.joinToString(" ")).append("\n")
        answer.append(colSum.joinToString(" ")).append("\n")
    }
    print(answer)
}