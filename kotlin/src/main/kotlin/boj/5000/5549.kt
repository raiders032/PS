package boj.`5000`

import java.util.StringTokenizer

/*
https://www.acmicpc.net/problem/5549
5549.행성 탐사
풀이1.1360ms
 */

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val k = readln().toInt()
    val board = Array(n) { CharArray(m) }
    val prefixSum = Array(n) { Array(m) { IntArray(3) { 0 } } }

    repeat(n) { i ->
        board[i] = readln().toCharArray()
    }

    for (i in  0 until n) {
        for (j in  0 until m) {
            prefixSum[i][j][0] = (if (j > 0) prefixSum[i][j - 1][0] else 0)  + (if (board[i][j] == 'J') 1 else 0)
            prefixSum[i][j][1] = (if (j > 0) prefixSum[i][j - 1][1] else 0)  + (if (board[i][j] == 'O') 1 else 0)
            prefixSum[i][j][2] = (if (j > 0) prefixSum[i][j - 1][2] else 0)  + (if (board[i][j] == 'I') 1 else 0)
        }
    }

    for (j in  0 until m) {
        for (i in  1 until n) {
            prefixSum[i][j][0] += prefixSum[i - 1][j][0]
            prefixSum[i][j][1] += prefixSum[i - 1][j][1]
            prefixSum[i][j][2] += prefixSum[i - 1][j][2]
        }
    }

    val answer = StringBuilder()
    repeat(k) {
        val stringTokenizer = StringTokenizer(readln())
        val x1 = stringTokenizer.nextToken().toInt() - 1
        val y1 = stringTokenizer.nextToken().toInt() - 1
        val x2 = stringTokenizer.nextToken().toInt() - 1
        val y2 = stringTokenizer.nextToken().toInt() - 1

        for (i in 0 until 3){
            var result = prefixSum[x2][y2][i]
            result -=  if (x1 > 0) prefixSum[x1 - 1][y2][i] else 0
            result -=  if (y1 > 0) prefixSum[x2][y1 - 1][i] else 0
            result +=  if (x1 > 0 && y1 > 0) prefixSum[x1 - 1][y1 - 1][i] else 0
            answer.append(result).append(" ")
        }
        answer.append("\n")
    }

    println(answer)
}
