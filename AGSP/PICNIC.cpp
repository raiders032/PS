#include<iostream>
#include<string.h>

using namespace std;

int N, M;
bool areFriends[10][10];
bool visited[10];

int makeCouple(int i, int n) {
	int ans = 0;

	if (n == N / 2) {
		return 1;
	}

	if (visited[i]) {
		return makeCouple(i+1,n);
	}

	for (int j = i + 1; j < N; j++) {
		if (!areFriends[i][j] || visited[j]) continue;
		visited[i] = visited[j] = true;
		ans += makeCouple(i + 1, n + 1);
		visited[i] = visited[j] = false;
	}

	return ans;
}

int main(void) {
	int tc;
	int x, y;

	cin >> tc;
	while (tc--) {
		cin >> N >> M;
		memset(areFriends, false, sizeof(areFriends));
		memset(visited, false, sizeof(visited));
		for (int i = 0; i < M; i++) {
			cin >> x >> y;
			areFriends[x][y] = areFriends[y][x] = true;
		}
		cout << makeCouple(0, 0)<<"\n";
	}
}

