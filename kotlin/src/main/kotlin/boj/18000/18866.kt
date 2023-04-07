package boj.`18000`

import java.lang.Integer.max
import java.lang.Integer.min
import kotlin.system.exitProcess

/*
https://www.acmicpc.net/problem/18866
18866.젊은 날의 생이여
풀이1.
 */

fun main() {
    val n = readln().toInt()
    val day = mutableListOf<Pair<Int, Int>>()
    var maxHappy = Int.MAX_VALUE
    var minSad = Int.MIN_VALUE

    repeat(n) {
        var (happy, sad) = readln().split(" ").map { it.toInt() }
        if (happy == 0){
            happy = maxHappy
            maxHappy -=1
        }

        if (sad == 0){
            sad = minSad
            minSad += 1
        }

        day.add(Pair(happy, sad))
    }

    var young = 0
    var old = n - 1

    var minYoungHappy = day[young].first
    var maxYoungSad = day[young].second

    var maxOldHappy = day[old].first
    var minOldSad = day[old].second

    if (minYoungHappy < maxOldHappy || maxYoungSad > minOldSad) {
        println(-1)
        exitProcess(0)
    }

    while (young + 1 < old) {
        val current = young + 1
        if (min(minYoungHappy, day[current].first) > maxOldHappy && max(maxYoungSad, day[current].second) < minOldSad) {
            young = current
            continue
        }

        old = current
        maxOldHappy = max(maxOldHappy, day[old].first)
        minOldSad = min(minOldSad, day[old].second)

        if (minYoungHappy < maxOldHappy || maxYoungSad > minOldSad) {
            println(-1)
            exitProcess(0)
        }

    }

    println(young + 1)
}