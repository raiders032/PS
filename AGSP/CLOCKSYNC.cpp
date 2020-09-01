#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

vector <int> clocks(16);
vector <int> visited(10, 0);
int ans = 987654321;
int switchs[10][5] = {
	{0,1,2,-1,-1},
	{3,7,9,11,-1},
	{4,10,14,15,-1},
	{0,4,5,6,7},
	{6,7,8,10,12},
	{0,2,14,15,-1},
	{3,14,15,-1,-1},
	{4,5,7,14,15},
	{1,2,3,4,5},
	{3,4,5,9,13}
};

void setButton(int num, int cmd) {
	visited[num] += cmd;
	if (cmd == 1) {
		for (int i = 0; i < 5; i++) {
			if (switchs[num][i] == -1)
				break;
			clocks[switchs[num][i]] = clocks[switchs[num][i]] == 12 ? 3 : clocks[switchs[num][i]] + 3;
		}
	}
	else {
		for (int i = 0; i < 5; i++) {
			if (switchs[num][i] == -1)
				break;
			clocks[switchs[num][i]] = clocks[switchs[num][i]] == 3 ? 12 : clocks[switchs[num][i]] - 3;
		}
	}
}

void solve(int x) {
	if (x == 10) {
		bool isOk = true;
		for (int i = 0; i < 16 && isOk; i++) {
			if (clocks[i] != 12)
				isOk = false;
		}

		if (isOk) {
			int sum = 0;
			for (int i = 0; i < 10; i++)
				sum += visited[i];
			ans = min(ans, sum);
		}

		return;
	}

	if (visited[x] >= 3) {
		solve(x + 1);
		return;
	}

	setButton(x, 1);
	solve(x);
	setButton(x, -1);

	solve(x + 1);

}

int main(void) {
	int tc;
	cin >> tc;
	while (tc--) {
		for (int i = 0; i < 16; i++)
			cin >> clocks[i];
		fill(visited.begin(), visited.end(), 0);
		ans = 987654321;
		solve(0);
		if (ans == 987654321)
			ans = -1;
		cout << ans << "\n";
	}
}