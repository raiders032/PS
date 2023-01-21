package boj.`17000`


/**
 * https://www.acmicpc.net/problem/17610
 * 17610.양팔저울
 * 풀이1.292ms
 */
fun main() {
    val n = readln().toInt()
    val numbers = readln().split(" ").map { it.toInt() }.toMutableList()
    val valid = BooleanArray(numbers.sum() + 1) { false }

    fun visit(level: Int, total: Int) {
        if (level == n) {
            if (total < 0)
                return

            valid[total] = true
            return
        }

        visit(level + 1, total + numbers[level])
        visit(level + 1, total - numbers[level])
        visit(level + 1, total)

    }

    visit(0, 0)
    println(valid.slice(1 until valid.size).count { !it })

}