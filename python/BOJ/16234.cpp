#include<iostream>
#include<vector>
#include<queue>
#include<string.h>
#include<math.h>

using namespace std;

int board[50][50];
int visited[50][50];
int N, L, R;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { -1,0,1,0 };

int move(int x, int y, int union_num) {
	int population = 0 , size = 0;
	queue <pair<int, int>> q;
	visited[x][y] = union_num;
	q.push(make_pair(x, y));

	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		population += board[x][y];
		size++;
		q.pop();

		for (int dir = 0; dir < 4; dir++) {
			int nx = x + dx[dir];
			int ny = y + dy[dir];
			if (0 > nx || nx >= N || 0 > ny || ny >= N) continue;
			if (visited[nx][ny]) continue;
			int diff = abs(board[x][y] - board[nx][ny]);
			if (diff < L || diff > R) continue;
			visited[nx][ny] = union_num;
			q.push(make_pair(nx, ny));
		}
	}

	if (size == 1) return 0;
	
	int after_move_population = population / size;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == union_num)
				board[i][j] = after_move_population;
		}
	}

	return 1;
}

int main(void) {
	int ans = 0;
	cin >> N >> L >> R;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}

	int moveable;
	int union_num;
	do {
		moveable = 0;
		union_num = 1;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					moveable += move(i, j, union_num++);
				}
			}
		}
		if (moveable) ans++;
		memset(visited, 0, sizeof(visited));
	} while (moveable);
	cout << ans;
}