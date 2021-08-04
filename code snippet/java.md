# 입출력

## BufferedReader

* Enter만 경계로 인식하고 타입은 String으로 고정

```java
BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

//String
String s = bf.readLine(); 
int i = Integer.parseInt(bf.readLine()); //Int

StringTokenizer st = new StringTokenizer(s); //StringTokenizer인자값에 입력 문자열 넣음
int a = Integer.parseInt(st.nextToken()); //첫번째 호출
int b = Integer.parseInt(st.nextToken()); //두번째 호출

String array[] = s.split(" "); //공백마다 데이터 끊어서 배열에 넣음
```

## StringTokenizer

```java
StringTokenizer st = new StringTokenizer("문자열", "구분자");

// 구분자 생략시 공백이 기본 구분자가 된다.
StringTokenizer st = new StringTokenizer("문자열"); 					

// 모든 token 접근 방식1
int countTokens = st.countTokens();
for (int i = 0; i < countTokens; i++) {
  String token = st.nextToken();
}

// 모든 token 접근 방식2
while (st.hasMoreTokens()){
  String token = st.nextToken();
}
```



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

int[] array = new int[100];
Arrays.fill(array, 10000);
```

```java
int[] array = {83, 90, 87};
```

```java
String[] names = null;
names = new String[] {"1", "2", "3"};
```



## 배열 정렬하기

```java
import java.util.Arrays;

String[] phone_book;
Arrays.sort(phone_book);
```

```java
int[][] lectures = new int[n][2];
Arrays.sort(lectures, Comparator.comparingInt(l -> l[0]));
```

```java
Integer [] nums = new Integer[n];
Arrays.sort(nums);
Arrays.sort(nums, Collections.reverseOrder());
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

# 우선순위 큐

```java
PriorityQueue<Integer> classroom = new PriorityQueue<>();

// Inserts the specified element into this priority queue.
classroom.add(classes[0][1]);

// 큐의 헤드 조회 원소를 삭제하지 않는다. 큐가 비었을 경우 null 반환
classroom.peek();

// 큐의 헤드 조회 및 원소 삭제, 큐가 비었을 경우 null 반환
classroom.poll();
```
