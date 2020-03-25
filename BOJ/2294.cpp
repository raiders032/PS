#include<iostream>
#include<memory.h>

using namespace std;

int main(void) {
	int N,K;
	int dp[10001];
	int coin[100];

	memset(dp, -1, sizeof(dp));
	cin >> N >> K;

	for (int i = 0; i < N; i++)
		cin >> coin[i];

	dp[0] = 0;
	for (int i = 0; i < 10000; i++) {
		if (dp[i] >= 0) {
			for (int j = 0; j < N; j++) {
				int ni = i + coin[j];
				if (ni > 10000) continue;
				if (dp[i] + 1 < dp[ni] || dp[ni] == -1) 
					dp[ni] = dp[i] + 1;
			}
		}
	}
	cout << dp[K];
}