# 문법



## for

```kotlin
for (i in array.indices) {
    println(array[i])
}
```

```kotlin
for ((index, value) in array.withIndex()) {
    println("the element at $index is $value")
}
```



## when

``````kotlin
when (i) {
  0 -> dfs(level + 1, result + numbers[level + 1])
  1 -> dfs(level + 1, result - numbers[level + 1])
  2 -> dfs(level + 1, result * numbers[level + 1])
  3 -> dfs(level + 1, result / numbers[level + 1])
}
``````

```kotlin
when {
  root1 < root2 -> disjointSet[root2] = root1
  root1 > root2 -> disjointSet[root1] = root2
  else -> {
    disjointSet[root1] = -1
    disjointSet[root2] = -1
  }
}
```



## Data Class

```kotlin
data class Point(val x: Int, val y: Int, val distance: Int)
```



# 자료구조



## 배열

```kotlin
val selfNumbers = Array<Boolean>(10001) { true }
```

```kotlin
val board = ArrayList<ArrayList<Int>>(n)
```

```kotlin
val dp = Array(n) { IntArray(n) { -1 } }
```

`````kotlin
val graph = Array(n) { mutableListOf<Int>() }
`````



## Duque

```kotlin
val deque = ArrayDeque<String>()
val deque = ArrayDeque<Pair<Int, Int>>().apply { add(1 to 0) }
```



## Queue

```kotlin
val queue = ArrayDeque<Pair<Int, Int>>().apply { add(1 to 0) }

queue.add(root)
queue.remove()
queue.element()
```



## PriorityQueue

```kotlin
val left = PriorityQueue<Int>(reverseOrder())
val right = PriorityQueue<Int>()

val priorityQueue = PriorityQueue<Triple<Int, Int, Int>>(compareBy { -it.third })
```



# 알고리즘



## 각 자리수 더하기

```kotlin
val sum = number.toString()
.map { Character.getNumericValue(it) }
.sum()
```



## 문자열의 각 캐릭터 수 구하기

```kotlin
  val word = "apple"
  val map = mutableMapOf<Char, Int>()

  for (char in word) {
      map.putIfAbsent(char, 0)
      map[char] = map[char]!! + 1
  }

  println(map)
```

```bash
{a=1, p=2, l=1, e=1}
```



## 문자열

