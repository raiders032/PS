#include<iostream>
#include<string.h>
using namespace std;

int R, C, T;
int board[50][50];
int after_board[50][50];
int fx,fy,sx,sy;
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

void diffuse() {
	memset(after_board, 0, sizeof(after_board));
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (board[i][j] == 0) continue;
			int cnt = 0;
			for (int dir = 0; dir < 4; dir++) {
				int nx = i + dx[dir];
				int ny = j + dy[dir];
				if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
				if ((nx == fx && ny == fy) || (nx == sx && ny == sy)) continue;
				after_board[nx][ny] += board[i][j] / 5;
				cnt++;
			}
			board[i][j] -= (board[i][j] / 5) * cnt;
		}
	}
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			board[i][j] += after_board[i][j];
		}
	}

}

void purify() {
	int dir = 0;
	int x = fx;
	int y = fy;
	while (true) {
		if ((x == 0 && y == 0) || (x == 0 && y == C - 1) || (x == fx && y == C - 1))
			dir++;
		int nx = x + dx[dir];
		int ny = y + dy[dir];
		if (nx == fx && ny == fy) {
			board[x][y] = 0;
			board[nx][ny] = -1;
			break;
		}
		board[x][y] = board[nx][ny];
		x = nx;
		y = ny;
	}
	dir = 2;
	x = sx;
	y = sy;
	while (true) {
		if ((x == R - 1 && y == 0) || (x == R - 1 && y == C - 1) || (x == sx && y == C - 1))
			dir = dir == 0 ? 3 : dir - 1;
		int nx = x + dx[dir];
		int ny = y + dy[dir];
		if (nx == sx && ny == sy) {
			board[x][y] = 0;
			board[nx][ny] = -1;
			break;
		}
		board[x][y] = board[nx][ny];
		x = nx;
		y = ny;
	}
}

int main(void) {
	int tmp;
	cin >> R >> C >> T;

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> tmp;
			if (tmp == -1) {
				fx = i-1;
				fy = j;
				sx = i;
				sy = j;
			}
			board[i][j] = tmp;
		
		}
	}

	for(int i=0;i<T;i++){
		diffuse();
		purify();
	}

	int ans = 0;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (board[i][j] == -1)continue;
			ans += board[i][j];
		}
	}
	cout << ans;
}