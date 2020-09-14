/*
	bfs
	1. 물고기가 있는지 확인
	2. 1마리면 그 물고기를 먹으러 간다.
	3. 1마리보다 많이면 거리가 가까운 물고기를 먹는다. 

*/
#include<iostream>
#include<string.h>
#include<queue>
#include<algorithm>

using namespace std;

int shark[2];
int board[20][20];
int visited[20][20];
int N;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

bool noFish() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (board[i][j] > 0)
				return false;
		}
	}
	return true;
}

bool cmp(const pair<int, int>& a, const pair<int, int>& b){
	if (a.first == b.first)
		return a.second < b.second;
	return a.first < b.first;
}

vector<pair<int, int>> findFish(int x, int y, int& minDist) {
	vector<pair<int, int>> fish;
	queue <pair<int, int>> q;
	visited[x][y] = 0;
	q.push(make_pair(x, y));
	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		q.pop();
		if (visited[x][y] >= minDist) break;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= N || ny <0 || ny >= N)
				continue;
			if (shark[0] < board[nx][ny] || visited[nx][ny] != -1)
				continue;
			visited[nx][ny] = visited[x][y] + 1;
			if ( 0 < board[nx][ny]  && board[nx][ny] < shark[0]) {
				fish.push_back(make_pair(nx, ny));
				minDist = min( minDist, visited[x][y] + 1);
			}
			q.push(make_pair(nx, ny));
		}
	}
	return fish;
}


bool moveAndEat(int& x, int& y, int& ans) {
	int minDist = 1000;
	vector<pair<int, int>> fish = findFish(x, y, minDist);
	
	if (fish.size() == 0) {
		return false;
	}

	sort(fish.begin(), fish.end(), cmp);
	x = fish.front().first;
	y = fish.front().second;
	ans += minDist;
	board[x][y] = 0;

	if (shark[0] == shark[1] + 1) {
		shark[0]++;
		shark[1] = 0;
	}
	else
		shark[1]++;
	return true;
}

int main(void) {
	int x, y, t = 0 ;
	int ans = 0;
	shark[0] = 2;
	shark[1] = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
			if (board[i][j] == 9) {
				x = i;
				y = j;
				board[i][j] = 0;
			}
		}
	}

	do {
		memset(visited, -1, sizeof(visited));
	}while (!noFish() && moveAndEat(x, y, ans));

	cout << ans;
}