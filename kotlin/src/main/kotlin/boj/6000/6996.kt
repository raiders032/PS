package boj.`6000`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val bufferedReader = BufferedReader(InputStreamReader(System.`in`))
    var n = Integer.parseInt(bufferedReader.readLine())

    while (n-- > 0) {
        val stringTokenizer = StringTokenizer(bufferedReader.readLine())
        val word1 = stringTokenizer.nextToken()
        val word2 = stringTokenizer.nextToken()
        var result = true

        if (word1.length != word2.length) {
            result = false
        } else if (word1.toCharArray().sort().toString() != word2.toCharArray().sort().toString()) {
            result = false
        }

        if (result)
            println("$word1 & $word2 are anagrams.")
        else
            println("$word1 & $word2 are NOT anagrams.")
    }
}

