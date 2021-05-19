/*
https://programmers.co.kr/learn/courses/30/lessons/42577
전화번호목록
레벨2
해시
풀이1
 */
package programmers.test.hash;

import java.util.Arrays;

public class 전화번호목록 {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for (int i = 1 ; i < phone_book.length; i++ ){
            if(phone_book[i].startsWith(phone_book[i-1]))
                return false;
        }
        return true;
    }
}