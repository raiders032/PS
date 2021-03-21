//6855. 신도시 전기 연결하기
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool cmp(int a, int b) {
	return a > b;
}

int main(void) {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		vector <int> dist;
		int N, K;
		cin >> N >> K;
		int pre, cur;
		cin >> pre;
		for (int i = 0; i < N - 1; i++) {
			cin >> cur;
			dist.push_back(cur - pre);
			pre = cur;
		}
		sort(dist.begin(), dist.end(), cmp);

		int ans = 0;
		for (int i = K - 1; i < N - 1; i++) {
			ans += dist[i];
		}
		cout << "#" << tc << " " << ans << "\n";
	}
}