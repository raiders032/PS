#include<iostream>
#include<stack>
#include<string>

using namespace std;

bool isOk(string str) {
	stack<char> stk;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '(' || str[i] == '[' || str[i] == '{')
			stk.push(str[i]);
		else {
			if (stk.empty())
				return false;

			if (str[i] == ')') {
				if (stk.top() != '(')
					return  false;
				else
					stk.pop();
			}
			else if (str[i] == ']') {
				if (stk.top() != '[')
					return  false;
				else
					stk.pop();
			}
			else if (str[i] == '}') {
				if (stk.top() != '{')
					return  false;
				else
					stk.pop();
			}
		}
	}
	return stk.empty();
}

int main(void) {
	int testCase;
	string str;
	cin >> testCase;
	while (testCase--) {
		cin >> str;
		if (isOk(str))
			cout << "YES" << "\n";
		else
			cout << "NO" << "\n";
	}
}