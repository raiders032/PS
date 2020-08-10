#include<iostream>

using namespace std;

int dice[4][3];
int board[20][20];
int dx[5] = {0,0,0,-1,1};
int dy[5] = {0,1,-1,0,0};
int N, M;

void roll_dice(int &x, int & y, int dir) {
	if (x + dx[dir] < 0 || x + dx[dir] >= N || y + dy[dir] < 0 || y + dy[dir] >= M)
		return;

	x += dx[dir];
	y += dy[dir];

	if (dir == 1) {
		swap(dice[1][2], dice[1][1]);
		swap(dice[1][1], dice[1][0]);
		swap(dice[1][0], dice[3][1]);
	}
	else if (dir == 2) {
		swap(dice[1][0], dice[3][1]);
		swap(dice[1][1], dice[1][0]);
		swap(dice[1][2], dice[1][1]);
	}
	else if (dir == 3) {
		swap(dice[0][1], dice[1][1]);
		swap(dice[0][1], dice[2][1]);
		swap(dice[0][1], dice[3][1]);
	}
	else if (dir == 4) {
		swap(dice[3][1], dice[2][1]);
		swap(dice[3][1], dice[1][1]);
		swap(dice[3][1], dice[0][1]);
	}
	
	if (board[x][y] == 0)
		board[x][y] = dice[3][1];
	else {
		dice[3][1] = board[x][y];
		board[x][y] = 0;
	}
	cout << dice[1][1] << "\n";
}

int main(void) {
	int x, y, K, dir;
	cin >> N >> M >> x >> y >> K;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> board[i][j];
		}
	}

	for (int i = 0; i < K; i++) {
		cin >> dir;
		roll_dice(x, y, dir);
	}
}