//3752. 가능한 시험 점수

#include<iostream>
#include<memory.h>

using namespace std;

bool visited[10001];
int main(void) {
	int T, N;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int arr[100];
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> arr[i];
		memset(visited, false, sizeof(visited));
		visited[0] = true;
		for (int i = 0; i < N; i++) {
			for (int j = 10000; j >= 0; j--) {
				if (visited[j])
					visited[j + arr[i]] = true;
			}
		}
		int ans = 0;
		for (int i = 0; i <= 10000; i++)
			if (visited[i])
				ans++;
		cout << "#" << tc << " " << ans << "\n";
	}
}