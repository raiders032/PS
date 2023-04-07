package boj.`7000`

fun main() {
    val answer = StringBuilder()
    var n = 0

    fun eval(expression: String): Int {
        expression.replace(" ", "")
        val indexOfFirst = expression.indexOfFirst { !it.isDigit() }
        var result = expression.subSequence(0, indexOfFirst).toString().toInt()
        var temp = 0

        for (char in expression.subSequence(indexOfFirst, expression.length)) {
            if (char.isDigit()) {
                temp = temp * 10 + char.digitToInt()
                continue
            }

            if (char == '+'){
                result += temp
                temp = 0
                continue
            }

            result -= temp
            temp = 0
        }

        return result

    }

    fun dfs(level: Int, expression: String) {
        if (level == n) {
            if (eval(expression) != 0)
                return

            answer.append(expression).append("\n")
        }

        dfs(level + 1, "${expression}+${level + 1}")
        dfs(level + 1, "${expression}-${level + 1}")
        dfs(level + 1, "${expression} ${level + 1}")
    }

    repeat(readln().toInt()) {
        n = readln().toInt()
        dfs(1, "1")
        answer.append("\n")
    }

    print(answer)

}