#include<iostream>
#include<vector>
#include<deque>

using namespace std;

int board[100][100];
char command[10001];
int currentDir = 1;
int N, K, L;
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };

deque <pair<int, int>> snake;

bool move() {
	int nx = snake.front().first + dx[currentDir];
	int ny = snake.front().second + dy[currentDir];
	if (nx < 0 || nx >= N || ny < 0 || ny >= N) return false;
	if (board[nx][ny] == 1) return false;
	if (board[nx][ny] == 0) {
		int tx = snake.back().first;
		int ty = snake.back().second;
		board[tx][ty] = 0;
		snake.pop_back();
	}
	board[nx][ny] = 1;
	snake.push_front(make_pair(nx, ny));
	return true;
}

int main(void) {
	int ans = 0, cnt =0;
	int x, y;
	cin >> N >> K;
	for (int i = 0; i < K; i++) {
		cin >> x >> y;
		board[x-1][y-1] = 2;
	}
	cin >> L;
	for (int i = 0; i < L; i++) {
		int x;
		char y;
		cin >> x >> y;
		command[x] = y;
	}
	snake.push_front(make_pair(0, 0));
	board[0][0] = 1;
	while (move()) {
		ans++;
		if (command[ans] == 'L') {
			currentDir = currentDir == 0 ? 3 : currentDir - 1;
		}
		if (command[ans] == 'D') {
			currentDir = currentDir == 3 ? 0 : currentDir + 1;
		}
	}
	cout << ans + 1;
}