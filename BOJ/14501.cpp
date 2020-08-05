#include<iostream>
#include<algorithm>
using namespace std;

int N;
int T[16];
int P[16];
int ans;

void solve(int day, int price) {
	if (day >= N + 1) {
		ans = max(ans, price);
		return;
	}
	if (day + T[day] <= N + 1) 
		solve(day + T[day], price + P[day]);
	else if(day + T[day] > N + 1)
		solve(day + T[day], price);
	solve(day + 1, price);
}

int main(void) {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> T[i] >> P[i];
	}
	solve(1,0);
	cout << ans;
}