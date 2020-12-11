#include<iostream>
#include<vector>
#include<memory.h>

using namespace std;

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
bool board[50][50];
bool visited[50][50];
int T, N, M, K;
void dfs(int x, int y) {
	visited[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || nx >= N || ny < 0 || ny >= M)
			continue;
		if (!visited[nx][ny] && board[nx][ny]) {
			dfs(nx, ny);
		}
	}
}

int main(void) {
	
	int x, y, ans;
	cin >> T;
	while (T--) {
		cin >> M >> N >> K;
		ans = 0;
		memset(board, false, sizeof(board));
		memset(visited, false, sizeof(visited));

		for (int i = 0; i < K; i++){
			cin >> y >> x;
			board[x][y] = true;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (!visited[i][j] && board[i][j]) {
					dfs(i, j);
					ans++;
				}
			}
		}
		cout << ans << "\n";
	}
}