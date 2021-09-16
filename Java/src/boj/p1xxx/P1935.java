package boj.p1xxx;

/*
https://www.acmicpc.net/problem/1935
1935.후위 표기식2
실버3
풀이2.132ms
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class P1935 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String express = br.readLine();
        double[] nums = new double[n];

        for (int i = 0; i < n; i++) {
            nums[i] = Double.parseDouble(br.readLine());
        }

        Stack<Double> stack = new Stack<>();
        for (char ch : express.toCharArray()) {
            if (ch == '*' || ch == '/' || ch == '+' || ch == '-'){
                double num1 = stack.pop();
                double num2 = stack.pop();

                if (ch == '*'){
                    stack.push(num2 * num1);
                }else if(ch == '/'){
                    stack.push(num2 / num1);
                }else if(ch == '+') {
                    stack.push(num2 + num1);
                }else{
                    stack.push(num2 - num1);
                }
            }
            else{
                stack.push(nums[ch - 'A']);
            }
        }
        System.out.printf("%.2f", stack.pop());
    }
}
