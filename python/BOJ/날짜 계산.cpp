#include<iostream>

using namespace std;

int main(void) {
	int e, s, m;
	int E, S, M;
	int ans;
	cin >> E >> S >> M;
	ans = s = m = e = E;
	while (s != S || m != M) {
		ans += 15;
		s = s + 15 <= 28 ? s + 15 : (s + 15) % 28;
		m = m + 15 <= 19 ? m + 15 : (m + 15) % 19;
	}
	cout << ans;
}