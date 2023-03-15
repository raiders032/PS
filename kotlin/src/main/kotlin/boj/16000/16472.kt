package boj.`16000`

import java.lang.Integer.max
/*
https://www.acmicpc.net/problem/16472
16472.고냥이
풀이1.248ms
 */
fun main() {
    val n = readln().toInt()
    val word = readln().toCharArray()
    val characterCount = mutableMapOf<Char, Int>()
    var left = 0
    var right = 0
    var answer = 0
    characterCount[word[left]] = 1

    while (right < word.size) {
        if (characterCount.size <= n) {
            answer = max(answer, right - left + 1)
            right += 1
            if (right < word.size) {
                characterCount.putIfAbsent(word[right], 0)
                characterCount[word[right]] = characterCount[word[right]]!! + 1
            }
        } else {
            characterCount[word[left]] = characterCount[word[left]]!! - 1
            if (characterCount[word[left]] == 0)
                characterCount.remove(word[left])
            left += 1
        }
    }

    println(answer)

}