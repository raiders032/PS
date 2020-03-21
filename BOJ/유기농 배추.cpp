#include<iostream>
#include<queue>

using namespace std; 
int board[50][50];
bool visited[50][50];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
int M, N, K;
void bfs(int x, int y) {
	queue <pair<int, int>> q;
	visited[x][y] = true;
	q.push(make_pair(x, y));
	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
			if (!visited[nx][ny] && board[nx][ny]) {
				visited[nx][ny] = true;
				q.push(make_pair(nx, ny));
			}
		}
	}
}


int main(void) {
	int T;
	cin >> T;
	while (T--) {
		int ans = 0;
		cin >> M >> N >> K;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				board[i][j] = 0;
				visited[i][j] = false;
			}
		}

		for (int k = 0; k < K; k++) {
			int x, y;
			cin >> x >> y;
			board[y][x] = 1;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (!visited[i][j] && board[i][j]) {
					bfs(i, j);
					ans++;
				}
			}
		}
		cout << ans <<"\n";
	}
}