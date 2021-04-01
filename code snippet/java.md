# 맵

## 맵 key값 카운트 하기

```java
import java.util.HashMap;
import java.util.Map;

Map<String, Integer> participants = new HashMap<>();

for (String name : participant) {
  participants.put(name, participants.getOrDefault(name, 0) + 1);
}
```



## 맵 모든 원소 조회

```java
import java.util.HashMap;
import java.util.Map;

Map<String, Integer> map = new HashMap<>();

for (String key : map.keySet()) {
  Integer value = map.get(key);
}
```



# 배열

## 배열 값 채우기

```java
import java.util.Arrays;

array = new int[100];
Arrays.fill(array, 10000);
```



## 배열 정렬하기

```java
import java.util.Arrays;

String[] phone_book;
Arrays.sort(phone_book);
```



## 배열 길이 구하기

```java
String[] phone_book;
int length = phone_book.length;
```

# 스택

```java
   Stack<Integer> stack = new Stack<>();
   stack.push(i);
   stack.peek()
   Integer index = stack.pop();
```



# 큐

```java
import java.util.LinkedList; 
import java.util.Queue; 

Queue<Integer> queue = new LinkedList<>();
queue.add(1); 
queue.peek();
queue.poll();
queue.isEmpty();
```



