package `4000`

/**
 * 4673.셀프 넘버
 * https://www.acmicpc.net/problem/4673
 * 풀이1.208ms
 */
fun main() {
    val isSelfNumber = Array(10001) { true }

    for (i in 1..10000) {
        val number = createNumber(i)
        isSelfNumber[number] = false
    }

    for (i in 1..10000) {
        if (isSelfNumber[i])
            println(i)
    }
}

fun createNumber(number: Int): Int {
    val result = number + number.toString()
        .map { Character.getNumericValue(it) }
        .sum()

    if (result > 10000)
        return 0

    return result
}