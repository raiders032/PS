package boj.`2000`

/*
https://www.acmicpc.net/problem/2529
2529.부등호
풀이1.148ms
 */
fun main() {
    val n = readln().toInt()
    val sign = readln().split(" ").toList()
    var visited = BooleanArray(10) { false }
    var selected = mutableListOf<Int>()

    fun findMax(level: Int): Boolean {
        if (selected.size == n + 1) {
            println(selected.joinToString(""))
            return true
        }

        for (number in 9 downTo 0) {
            if (visited[number]) {
                continue
            }

            if (selected.isEmpty()) {
                visited[number] = true
                selected.add(number)
                if (findMax(0))
                    return true
                visited[number] = false
                selected.removeLast()
                continue
            }

            val last = selected.last()
            if (sign[level] == "<" && last < number) {
                visited[number] = true
                selected.add(number)
                if (findMax(level + 1))
                    return true
                visited[number] = false
                selected.removeLast()
                continue
            }

            if (sign[level] == ">" && last > number) {
                visited[number] = true
                selected.add(number)
                if (findMax(level + 1))
                    return true
                visited[number] = false
                selected.removeLast()
                continue
            }
        }

        return false
    }

    fun findMin(level: Int): Boolean {
        if (selected.size == n + 1) {
            println(selected.joinToString(""))
            return true
        }

        for (number in 0..9) {
            if (visited[number]) {
                continue
            }

            if (selected.isEmpty()) {
                visited[number] = true
                selected.add(number)
                if (findMin(0))
                    return true
                visited[number] = false
                selected.removeLast()
                continue
            }

            val last = selected.last()
            if (sign[level] == "<" && last < number) {
                visited[number] = true
                selected.add(number)
                if (findMin(level + 1))
                    return true
                visited[number] = false
                selected.removeLast()
                continue
            }

            if (sign[level] == ">" && last > number) {
                visited[number] = true
                selected.add(number)
                if (findMin(level + 1))
                    return true
                visited[number] = false
                selected.removeLast()
                continue
            }
        }

        return false
    }

    findMax(0)
    visited = BooleanArray(10) { false }
    selected = mutableListOf()
    findMin(0)
}

