#include<iostream>
#include<vector>
#include <stdio.h>

using namespace std;

int main(void) {
	int arr[1000000];
	int N, B, C;
	long long ans;
	scanf("%d", &N);
	ans = N;
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	cin >> B >> C;
	for (int i = 0; i < N; i++) {
		arr[i] -= B;
		if (arr[i] > 0)
			ans += arr[i] % C == 0 ? arr[i] / C : arr[i] / C + 1;
	}
	cout << ans;
}