#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool cmp(int a, int b) {
	return a > b;
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int T,N;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N;
		vector <int> arr(N);
		for (int i = 0; i < N; i++) 
			cin >> arr[i];
		sort(arr.begin(), arr.end(),cmp);
		int sum = 0;
		for (int i = 0; i < N; i++) {
			if (i % 3 == 2) continue;
			sum += arr[i];
		}
		cout << "#" << tc << " " << sum << "\n";
	}
}