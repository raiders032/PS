#include<iostream>
using namespace std;
int block[12][4] = {
	{-1,0,0,1},
	{0,1,1,0},
	{0,-1,1,0},
	{0,-1,-1,0},

	{-1,0,-1,-1},
	{0,1,1,1},
	{1,0,1,-1},
	{0,-1,-1,-1},

	{-1,-1,-1,0},
	{0,1,-1,1},
	{1,0,1,1},
	{0,-1, 1,-1},
};

char board[20][20];
int H, W;

int coverBlock(int x, int y) {
	int cnt = 0;
	if (x == H && y == 0)
		return 1;
	if (board[x][y] == '#') {
		return coverBlock(y == W - 1 ? x + 1 : x, y == W - 1 ? 0 : y + 1);
	}
	for (int dir = 0; dir < 12; dir++) {
		int nextX = x + block[dir][0];
		int nextY = y + block[dir][1];
		int nextX2 = x + block[dir][2];
		int nextY2= y + block[dir][3];
		if (nextX < 0 || nextX >= H || nextY < 0 || nextY >= W)
			continue;
		if (nextX2 < 0 || nextX2 >= H || nextY2 < 0 || nextY2 >= W)
			continue;
		if (board[nextX][nextY] == '#' || board[nextX2][nextY2] == '#')
			continue;
		board[x][y] = board[nextX][nextY] = board[nextX2][nextY2] = '#';
		cnt += coverBlock(y == W - 1 ? x + 1 : x, y == W - 1 ? 0 : y + 1);
		board[x][y] = board[nextX][nextY] = board[nextX2][nextY2] = '.';
	}
	return cnt;
}

int main(void) {
	int C;
	cin >> C;
	while (C--) {
		cin >> H >> W;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				cin >> board[i][j];
			}
		}
		cout << coverBlock(0, 0)<<"\n";
	}
}