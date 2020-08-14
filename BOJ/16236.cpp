#include<iostream>
#include<queue>
#include<string.h>

using namespace std;
int N, ans;
int board[20][20];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
int shark[2];

bool move(int& x, int& y) {
	int visited[20][20];
	bool find = false;
	queue <pair<int, int>> q;
	memset(visited, -1, sizeof(visited));
	visited[x][y] = board[x][y] = 0;
	q.push(make_pair(x, y));

	while (!q.empty() && !find) {
		x = q.front().first;
		y = q.front().second;
		q.pop();
		for (int dir = 0; dir < 4; dir++) {
			int nx = x + dx[dir];
			int ny = y + dy[dir];

			if (nx < 0 || nx >= N || ny < 0 || ny >= N)
				continue;

			if (visited[nx][ny] != -1 || shark[0] < board[nx][ny])
				continue;

			if (board[nx][ny] < shark[0] && board[nx][ny] > 0) {
				if (shark[0] == shark[1] + 1) {
					shark[0]++;
					shark[1] = 0;
				}
				else {
					shark[1]++;
				}
				ans += visited[x][y] + 1;
				x = nx;
				y = ny;
				find = true;
				break;
			}

			visited[nx][ny] = visited[x][y] + 1;
			q.push(make_pair(nx, ny));
		}
	}
	return find;
}

int main(void) {

	int x, y, tmp;

	cin >> N;
	shark[0] = 2;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> tmp;
			board[i][j] = tmp;
			if (tmp == 9) {
				x = i;
				y = j;
			}
		}
	}

	while (move(x, y)) {
	}

	cout << ans;
}