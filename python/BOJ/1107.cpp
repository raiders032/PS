#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

bool broken[10];

int isValid(int n) {
	string str = to_string(n);
	int len = str.size();
	for (int i = 0; i < len; i++) {
		if (broken[str[i] - '0'])
			return 0;
	}
	return len;
}

int main(void) {
	int N, M, ans;
	cin >> N >> M;
	ans = abs(N - 100);
	for (int i = 0; i < M; i++) {
		int tmp;
		cin >> tmp;
		broken[tmp] = true;
	}

	for (int i = 0; i <= 1000000; i++) {
		int num = isValid(i);
		if (num == 0)
			continue;
		ans = min(ans, abs(N - i) + num);
	}

	cout << ans;
}