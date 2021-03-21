#include<iostream>
#include<queue>

using namespace std;

int main(void) {
	int testCase;
	int N, K;
	cin >> testCase;

	while (testCase--) {
		queue<int> q;
		cin >> N >> K;

		for (int i = 1; i <= N; i++) {
			q.push(i);
		}

		while (q.size() > 2) {
			q.pop();
			for (int i = 0; i < K - 1; i++) {
				int tmp = q.front();
				q.pop();
				q.push(tmp);
			}
		}
		if (q.front() < q.back())
			cout << q.front() << " " << q.back() << "\n";
		else
			cout << q.back() << " " << q.front() << "\n";
	}
}