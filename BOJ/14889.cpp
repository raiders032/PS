#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;

int main(void) {
	int N;
	int teamS[2];
	int ans = INT_MAX;
	vector <vector <int>> board;
	
	cin >> N;
	board.resize(N);
	for (int i = 0; i < N; i++) {
		board[i].resize(N);
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}

	vector<int> team(N,0);
	fill(team.begin() + N / 2, team.end(), 1);

	do {
		teamS[0] = teamS[1] = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i == j) continue;
				if (team[i] != team[j]) continue;
				teamS[team[i]] += board[i][j];
			}
		}
		int diff = abs(teamS[0] - teamS[1]);
		ans = ans < diff ? ans : diff;
	} while (next_permutation(team.begin(),team.end()));

	cout << ans;
}