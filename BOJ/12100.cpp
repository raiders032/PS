#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int ans = 0;
int N;
vector <vector<int>> board;
int dx[4] = {0,-1,0,1};
int dy[4] = {-1,0,1,0};

void moveCell(int dir, int x, int y, vector<vector<int>> & board) {
	int nx = x - dx[dir];
	int ny = y - dy[dir];
	while (nx >= 0 && nx < N && ny < N && ny >= 0){
		if (board[nx][ny] != 0) break;
		if (nx -dx[dir] < 0 || nx - dx[dir] >= N || ny - dy[dir] >= N || ny - dy[dir] < 0) break;
		nx -= dx[dir];
		ny -= dy[dir];
	}
	if (board[x][y] == 0) {
		board[x][y] = board[nx][ny];
		board[nx][ny] = 0;
		return;
	}
	if (board[x][y] == board[nx][ny]) {
		board[x][y] *= 2;
		board[nx][ny] = 0;
		return;
	}
}

void move(int dir, vector<vector<int>> & board) {
	int x, y;
	if (dir == 0) {
		for (x = 0; x < N; x++) {
			for (y = 0; y < N - 1; y++) {
				if (board[x][y] == 0) {
					moveCell(dir, x, y, board);
				}
				moveCell(dir, x, y, board);
			}
		}
	}
	else if (dir == 1) {
		for (y = 0; y < N; y++) {
			for (x = 0; x < N - 1; x++) {
				if (board[x][y] == 0) {
					moveCell(dir, x, y, board);
				}
				moveCell(dir, x, y, board);
			}
		}
	}
	else if (dir == 2) {
		for (x = 0; x < N; x++) {
			for (y = N - 1; y > 0; y--) {
				if (board[x][y] == 0) {
					moveCell(dir, x, y, board);
				}
				moveCell(dir, x, y, board);
			}
		}
	}
	else if (dir == 3) {
		for (y = 0; y < N; y++) {
			for (x = N - 1; x > 0; x--) {
				if (board[x][y] == 0) {
					moveCell(dir, x, y, board);
				}
				moveCell(dir, x, y, board);
			}
		}
	}
}

void solve(int cnt, vector<vector<int>> board) {
	if (cnt == 5) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				ans = max(ans, board[i][j]);
			}
		}
		return;
	}
	vector<vector<int>> org = board;
	for (int dir = 0; dir < 4; dir++) {
		move(dir, board);
		solve(cnt + 1, board);
		board = org;
	}
}

int main(void) {
	cin >> N;
	board.resize(N);
	for (int i = 0; i < N; i++) {
		board[i].resize(N);
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}
	solve(0, board);
	cout<<ans;
}