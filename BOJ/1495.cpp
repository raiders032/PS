#include<iostream>

using namespace std;
bool dp[1001][101];

int main(void) {
	int N, S, M;
	int V[100];
	cin >> N >> S >> M;
	dp[S][0] = true;

	for (int i = 0; i < N; i++)
		cin >> V[i];

	for (int n = 0; n < N; n++) {
		for (int v = 0; v <= M; v++) {
			if (dp[v][n]) {
				if (v + V[n] <= M) {
					dp[v + V[n]][n + 1] = true;
				}
				if (v - V[n] >= 0) {
					dp[v - V[n]][n + 1] = true;
				}
			}
		}
	}

	int ans = -1;
	for (int i = M; i >= 0; i--) {
		if (dp[i][N]) {
			ans = i;
			break;
		}
	}
	cout << ans;
}