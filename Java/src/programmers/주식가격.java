/*
https://programmers.co.kr/learn/courses/30/lessons/42584?language=java
주식가격
레벨2
스택
풀이1
 */
package programmers;

import java.util.Arrays;
import java.util.Stack;

public class 주식가격 {
    public static void main(String[] args) {
        int[] solution = new 주식가격().solution(new int[]{1, 2, 3, 2, 3});
        System.out.println(Arrays.toString(solution));
    }

    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < prices.length ; i++){
            while (!stack.empty() && prices[i] < prices[stack.peek()]){
                Integer index = stack.pop();
                answer[index] = i - index;
            }
            stack.push(i);
        }

        while (!stack.empty()){
            Integer index = stack.pop();
            answer[index] = prices.length - index - 1;
        }

        return answer;
    }
}
