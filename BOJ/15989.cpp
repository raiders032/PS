#include<iostream>
#include<memory.h>
using namespace std;

int main(void) {
	int dp[10001];
	memset(dp, 0, sizeof(dp));
	dp[0] = 1;
	for (int i = 1; i <= 3; i++) {
		for (int j = i; j <= 10000; j++)
			dp[j] += dp[j - i];
	}
	
	int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		cout << dp[N] << "\n";
	}
}