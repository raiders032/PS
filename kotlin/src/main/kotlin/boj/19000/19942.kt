package boj.`19000`

/*
https://www.acmicpc.net/problem/19942
19942.다이어트
풀이1.248ms
*/
fun main() {
    val n = readln().toInt()
    val limits = readln().split(" ").map { it.toInt() }.toList()
    val ingredients = mutableListOf<MutableList<Int>>()
    val totals = IntArray(5) { 0 }
    var selected = ArrayDeque<Int>()
    var minCost = Int.MAX_VALUE
    var minList = ""

    fun dfs(level: Int) {
        if (level == n) {
            for (i in 0 until 4) {
                if (totals[i] < limits[i])
                    return
            }

            when {
                totals[4] < minCost -> {
                    minCost = totals[4]
                    minList = selected.joinToString(" ")
                }

                totals[4] == minCost -> {
                    minCost = totals[4]
                    val selectedString = selected.joinToString(" ")
                    minList = if (selectedString < minList) selected.joinToString(" ") else minList
                }
            }

            return
        }

        repeat(5) {
            totals[it] += ingredients[level][it]
        }

        selected.addLast(level + 1)
        dfs(level + 1)


        selected.removeLast()
        repeat(5) {
            totals[it] -= ingredients[level][it]
        }

        dfs(level + 1)

    }

    repeat(n) {
        ingredients.add(readln().split(" ").map { it.toInt() }.toMutableList())
    }

    dfs(0)
    when (minCost) {
        Int.MAX_VALUE -> println(-1)
        else -> {
            println(minCost)
            println(minList)
        }
    }

}