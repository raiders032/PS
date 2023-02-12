package boj.`2000`

import java.util.*

/*
https://www.acmicpc.net/problem/2800
2800.괄호 제거
풀이1.228ms
 */
var n = 0
val parentheses = mutableListOf<Pair<Int, Int>>()
val selected = Stack<Pair<Int, Int>>()
val expression = readln()
val answer = mutableSetOf<String>()
fun main() {
    val stack = Stack<Int>()

    for ((index, char) in expression.withIndex()) {
        when (char) {
            '(' -> stack.push(index)
            ')' -> parentheses.add(Pair(stack.pop(), index))
        }
    }

    n = parentheses.size
    dfs(0)
    println(answer.toMutableList().sorted().joinToString("\n"))
}

fun dfs(level: Int) {
    if (level == n) {
        if (selected.empty())
            return

        val toCharArray = expression.toCharArray()

        for (parentheses in selected) {
            toCharArray[parentheses.first] = 'X'
            toCharArray[parentheses.second] = 'X'
        }

        answer.add(toCharArray.joinToString().replace("X", ""))
        return
    }

    selected.push(parentheses[level])
    dfs(level + 1)

    selected.pop()
    dfs(level + 1)
}