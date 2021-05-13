/*
https://programmers.co.kr/learn/courses/30/lessons/42576
완주하지 못한 선수
레벨1
해시
 */

package programmers.test.hash;

import java.util.HashMap;
import java.util.Map;

public class 완주하지못한선수 {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String,Integer> participants = new HashMap<>();

        for (String name : participant){
            participants.put(name, participants.getOrDefault(name, 0) + 1);
        }

        for (String name: completion){
            if (participants.get(name).equals(1))
                participants.remove(name);
            else{
                participants.replace(name, participants.get(name) - 1);
            }
        }

        return participants.keySet().iterator().next();
    }
}
