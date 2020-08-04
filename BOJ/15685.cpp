#include<iostream>
#include<vector>

using namespace std;

bool board[101][101];
int dx[4] = { 0,-1,0,1 };
int dy[4] = { 1,0,-1,0 };

void move(int x, int y, int d, int g) {
	vector <int> curve;
	board[x][y] = true;
	curve.push_back(d);
	x += dx[d];
	y += dy[d];
	for (int i = 1; i <= g; i++) {
		for (int j = curve.size() - 1; j >= 0; j--) {
			board[x][y] = true;
			d = (curve[j] + 1) % 4;
			curve.push_back(d);
			x += dx[d];
			y += dy[d];
		}
	}
	board[x][y] = true;
}

int main(void) {
	int N,x,y,d,g;
	int ans = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> y >> x >> d >> g;
		move(x, y, d, g);
	}
	for (int i = 0; i <= 99; i++) {
		for (int j = 0; j <= 99; j++) {
			if (board[i][j] && board[i][j+1] && board[i+1][j] && board[i+1][j+1])
				ans++;
		}
	}
	cout << ans;
}