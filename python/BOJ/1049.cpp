//1049 ±‚≈∏¡Ÿ
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(void) {
	int N, M;
	vector <int> p6;
	vector <int> p1;
	cin >> N >> M;
	p6.resize(M);
	p1.resize(M);
	for (int i = 0; i < M; i++) {
		cin >> p6[i] >> p1[i];
	}
	sort(p6.begin(), p6.end());
	sort(p1.begin(), p1.end());
	if (p1[0] * 6 <= p6[0]) {
		cout << N * p1[0];
	}
	else {
		if (N % 6 * p1[0] < p6[0])
			cout << (N / 6 * p6[0]) + (N % 6 * p1[0]);
		else
			cout << (N / 6 + 1) * p6[0];
	}
}