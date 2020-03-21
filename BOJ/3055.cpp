#include<iostream>
#include<vector>
#include<queue>

using namespace std;

typedef struct _node {
	int x;
	int y;
	int type;
}node;

char board[50][50];
int visited[50][50];
int R, C;
vector <node> water;

void solve(int x, int y, int type) {
	int dx[4] = { 0,0,1,-1 };
	int dy[4] = { 1,-1,0,0 };
	queue <node> q;
	visited[x][y] = 0;
	for (int i = 0; i < water.size(); i++) {
		q.push({ water[i].x, water[i].y, water[i].type });
	}
	q.push({ x, y,type });
	while (!q.empty()) {
		x = q.front().x;
		y = q.front().y;
		type = q.front().type;
		q.pop();
		if (board[x][y] == 'D') {
			cout << visited[x][y];
			return;
		}
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= R || ny < 0 || ny >= C)
				continue;
			if (board[nx][ny] == 'X')
				continue;
			if (type == 0) {
				if (board[nx][ny] != '*' && visited[nx][ny] == -1) {
					visited[nx][ny] = visited[x][y] + 1;
					q.push({ nx,ny,0 });
				}
			}
			else {
				if (board[nx][ny] == '.') {
					board[nx][ny] = '*';
					q.push({ nx,ny,1 });
				}
			}
		}
	}
	cout << "KAKTUS";
	return;
}

int main(void) {
	int x, y;
	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> board[i][j];
			if (board[i][j] == 'S') {
				x = i;
				y = j;
				board[i][j] = '.';
			}
			else if (board[i][j] == '*') {
				water.push_back({ i,j,1 });
			}
			visited[i][j] = -1;
		}
	}
	solve(x, y, 0);
}