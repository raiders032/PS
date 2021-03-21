#include<iostream>

using namespace std;

int board[100][100];
long long dp[100][100];

int main(void) {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}
	dp[0][0] = 1;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (dp[i][j] == 0) continue;
			if (board[i][j] == 0)break;
			if (j + board[i][j] < N) {
				dp[i][j + board[i][j]] += dp[i][j];
			}
			if (i + board[i][j] < N) {
				dp[i + board[i][j]][j] += dp[i][j];
			}
		}
	}
	cout << dp[N - 1][N - 1];
}