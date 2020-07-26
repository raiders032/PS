#include<iostream>
#include<queue>

using namespace std;

struct position {
	int rx, ry;
	int bx, by;
	int cnt;
};

char board[10][10];
int dx[4] = { 0,1,0,-1 };
int dy[4] = { -1,0,1,0 };
int pos[3][2];
bool visited[10][10][10][10];

int move(int dir, int& x, int& y) {
	int dist = 0;
	while (board[x + dx[dir]][y + dy[dir]] != '#') {
		if (board[x + dx[dir]][y + dy[dir]] == 'O')
			return -1;
		dist++;
		x = x + dx[dir];
		y = y + dy[dir];
	}
	return dist;
}

void solve(int rx, int ry, int bx, int by, int cnt) {
	visited[rx][ry][bx][by] = true;
	queue<position> q;
	q.push({ rx,ry,bx,by,cnt });
	while (!q.empty()) {
		rx = q.front().rx;
		ry = q.front().ry;
		bx = q.front().bx;
		by = q.front().by;
		cnt = q.front().cnt;
		q.pop();
		if (cnt >= 10) {
			cout << -1;
			return;
		}
		for (int dir = 0; dir < 4; dir++) {
			int nrx = rx, nry = ry, nbx = bx, nby = by;
			int redDist = move(dir, nrx, nry);
			int blueDist = move(dir, nbx, nby);
			if (blueDist == -1) continue;
			if (blueDist == 0 && redDist == 0) continue;
			if (redDist == -1) {
				cout << cnt + 1;
				return;
			}
			if (nrx == nbx && nry == nby) {
				if (redDist > blueDist) {
					nrx -= dx[dir];
					nry -= dy[dir];
				}
				else {
					nbx -= dx[dir];
					nby -= dy[dir];
				}
			}
			if (visited[nrx][nry][nbx][nby]) continue;
			q.push({ nrx,nry,nbx,nby,cnt + 1 });
		}
	}
	cout << -1;
}



int main() {
	int N, M;
	char tmp;
	position pos;
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> tmp;
			board[i][j] = tmp;
			if (tmp == 'R') {
				pos.rx = i;
				pos.ry = j;
			}
			else if (tmp == 'B') {
				pos.bx = i;
				pos.by = j;
			}
		}
	}
	solve(pos.rx, pos.ry, pos.bx, pos.by, 0);

}