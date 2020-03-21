#include <deque>
#include<iostream>
#include<cstdio>

using namespace std;

int board[100][100];
int visited[100][100];
int N, M;

void solve() {
	int x, y;
	int dx[4] = {0, 0, 1, -1};
	int dy[4] = {1, -1, 0, 0};
	deque <pair<int, int>> dq;
	visited[0][0] = 0;
	dq.push_back(make_pair(0, 0));
	while (!dq.empty()) {
		x = dq.front().first;
		y = dq.front().second;
		dq.pop_front();
		if (x == N - 1 && y == M - 1) {
			cout << visited[x][y];
			return;
		}
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= N || ny < 0 || ny >= M)
				continue;
			if (visited[nx][ny] == -1) {
				if (board[nx][ny]) {
					visited[nx][ny] = visited[x][y] + 1;
					dq.push_back(make_pair(nx,ny));
				}
				else {
					visited[nx][ny] = visited[x][y];
					dq.push_front(make_pair(nx, ny));
				}
			}
		}
	}
	return;
}

int main(void) {
	cin >> M >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &board[i][j]);
			visited[i][j] = -1;
		}
	}
	solve();
}