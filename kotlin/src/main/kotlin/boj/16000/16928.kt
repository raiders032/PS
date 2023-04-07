package boj.`16000`

/*
https://www.acmicpc.net/problem/16928
16928.뱀과 사다리 게임
풀이1.180ms
 */

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val jump = mutableMapOf<Int, Int>()
    val visited = BooleanArray(101) { false }

    repeat(n + m) {
        val (from, to) = readln().split(" ").map { it.toInt() }
        jump[from] = to
    }

    val queue = ArrayDeque<Pair<Int, Int>>().apply { add(1 to 0) }
    visited[1] = true

    while (queue.isNotEmpty()) {
        val (x, distance) = queue.removeFirst()

        if (x == 100) {
            println(distance)
            break
        }

        for (dx in 1..6) {
            var nx = x + dx
            if (nx > 100 || visited[nx]) continue
            visited[nx] = true
            queue.add(Pair(nx, distance + 1))

            while(jump.containsKey(nx)) {
                queue.removeLast()
                val nnx = jump[nx]!!
                if (visited[nnx]) break
                visited[nnx] = true
                queue.add(Pair(nnx, distance + 1))
                nx = nnx
            }

        }
    }

}

