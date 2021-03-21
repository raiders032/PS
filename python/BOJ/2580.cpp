//2580 ½ºµµÄí
#include<iostream>
#include<vector>

using namespace std;

int board[9][9];
bool r_visited[9][10];
bool c_visited[9][10];
bool s_visited[9][10];
vector <pair <int, int>> blank;

void dfs(int len, int cnt) {
	if (len == cnt) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				cout << board[i][j] << " ";
			}
			cout << "\n";
		}
		exit(0);
	}
	int x, y;
	x = blank[cnt].first;
	y = blank[cnt].second;

	for (int i = 1; i < 10; i++) {
		if (r_visited[x][i] || c_visited[y][i] || s_visited[x / 3 * 3 + y / 3][i]) continue;
		r_visited[x][i] = c_visited[y][i] = s_visited[x / 3 * 3 + y / 3][i] = true;
		board[x][y] = i;
		dfs(len, cnt + 1);
		board[x][y] = 0;
		r_visited[x][i] = c_visited[y][i] = s_visited[x / 3 * 3 + y / 3][i] = false;
		
	}
}

int main(void) {

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			int tmp;
			cin >> tmp;
			board[i][j] = tmp;
			if (tmp != 0) {
				r_visited[i][tmp] = true;
				c_visited[j][tmp] = true;
				s_visited[i / 3 * 3 + j / 3][tmp] = true;
			}
			else {
				blank.push_back(make_pair(i, j));
			}
		}
	}

	int len = blank.size();
	dfs(len, 0);
}