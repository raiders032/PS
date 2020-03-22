//14592 ¿¬±¸¼Ò

#include<iostream>
#include<vector>
#include<memory.h>
#include<queue>

using namespace std;

vector <pair<int, int>> virus;
vector <vector <int>> board;
int N, M;
bool visited[8][8];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int ans = 0;

int bfs(int safe_area) {
	int x, y;
	memset(visited, false, sizeof(visited));
	queue <pair<int, int>> q;
	for (int i = 0; i < virus.size(); i++) {
		x = virus[i].first;
		y = virus[i].second;
		visited[x][y] = true;
		q.push(make_pair(x, y));
	}
	while (!q.empty()) {
		if (safe_area < ans)
			return 0;
		x = q.front().first;
		y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= N || ny < 0 || ny >= M)
				continue;
			if (!visited[nx][ny] && board[nx][ny] == 0) {
				visited[nx][ny] = true;
				q.push(make_pair(nx, ny));
				safe_area--;
			}
		}
	}
	return safe_area;
}

int main(void) {
	int safe_area = 0;
	cin >> N >> M;
	board.resize(N);
	for (int i = 0; i < N; i++) {
		board[i].resize(M);
		for (int j = 0; j < M; j++) {
			cin >> board[i][j];
			if (board[i][j] == 2)
				virus.push_back(make_pair(i,j));
			if (board[i][j] == 0)
				safe_area++;
		}
	}
	safe_area -= 3;
	for (int i = 0; i < N * M - 2; i++) {
		if (board[i / M][i % M] != 0) continue;
		for (int j = i + 1; j < N * M - 1; j++) {
			if (board[j / M][j % M] != 0) continue;
			for (int k = j + 1; k < N * M; k++) {
				if (board[k / M][k % M] != 0) continue;
				board[i / M][i % M] = board[j / M][j % M] = board[k / M][k % M] = 1;
				int cnt = bfs(safe_area);
				ans = ans > cnt ? ans : cnt;
				board[i / M][i % M] = board[j / M][j % M] = board[k / M][k % M] = 0;
			}
		}
	}

	cout << ans;
}