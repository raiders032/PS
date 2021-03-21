//1218. °ýÈ£ Â¦Áþ±â
#include <iostream>
#include <stack>
using namespace std;

int main(void) {
	for (int tc = 1; tc <= 10; tc++) {
		stack <char> stk;
		bool ok = true;
		int N;
		cin >> N;
		for (int i = 0; i < N; i++) {
			char tmp;
			cin >> tmp;
			if (!ok) continue;
			if (tmp == '{' || tmp == '[' || tmp == '(' || tmp == '<') {
				stk.push(tmp);
			}
			else {
				if (stk.top() == '{' && tmp =='}') {
					stk.pop();
					continue;
				}
				else if (stk.top() == '[' && tmp == ']') {
					stk.pop();
					continue;
				}
				else if (stk.top() == '(' && tmp == ')') {
					stk.pop();
					continue;
				}
				else if (stk.top() == '<' && tmp == '>') {
					stk.pop();
					continue;
				}
				ok = false;
			}
		}
		if (ok && stk.empty())
			cout << "#" << tc << " " << 1 << "\n";
		else
			cout << "#" << tc << " " << 0 << "\n";
	}
}