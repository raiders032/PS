#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N, M, K;
int board[11][11];
int fertilizer[11][11];
vector <vector<vector<int>>> tree;

int dx[8] = {-1,-1,-1,0,1,1,1,0};
int dy[8] = {-1,0,1,1,1,0,-1,-1};

int main(void) {
	cin >> N >> M >> K;
	tree.resize(N);
	fill(&board[0][0],&board[10][11], 5);

	for (int i = 0; i < N; i++) {
		tree[i].resize(N);
		for (int j = 0; j < N; j++) {
			cin >> fertilizer[i][j];
		}
	}

	for (int i = 0; i < M; i++){
		int x, y, age;
		cin >> x >> y >> age;
		tree[x-1][y-1].push_back(age);
	}

	for (int year = 0; year < K; year++) {

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int size = tree[i][j].size();
				if (size == 0) continue;
				sort(tree[i][j].begin(), tree[i][j].end());
				int k;
				int fertilizer = 0;

				for (k = 0; k < size; k++) {
					if (tree[i][j][k] > board[i][j]) break;
					board[i][j] -= tree[i][j][k];
					tree[i][j][k] += 1;	
				}

				for (int l = k; l < size; l++)
					fertilizer += tree[i][j][l];
				board[i][j] += fertilizer / 2;

				tree[i][j].erase(tree[i][j].begin() + k, tree[i][j].end());
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				board[i][j] += fertilizer[i][j];
				int size = tree[i][j].size();
				if (size == 0) continue;
				for (int k = 0; k < size; k++) {
					if (tree[i][j][k] % 5 != 0) continue;
					for (int dir = 0; dir < 8; dir++) {
						int nx = i + dx[dir];
						int ny = j + dy[dir];
						if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
						tree[nx][ny].push_back(1);
					}
				}
			}
		}
	}

	int ans = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			ans += tree[i][j].size();
		}
	}
	cout << ans;
}