#include<iostream>
#include<vector>
#include<algorithm>
#include<limits.h>

using namespace std;

int main(void) {
	int N, M, K, ans = INT_MAX;
	int board[50][50];
	int tmp;
	vector <pair<int,int>> house;
	vector <pair<int, int>> chicken;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> tmp;
			board[i][j] = tmp;
			if (tmp == 2)
				chicken.push_back(make_pair(i, j));
			else if (tmp == 1)
				house.push_back(make_pair(i, j));
		}
	}
	
	int c_size = chicken.size();
	int h_size = house.size();

	vector <int> selected(c_size, 0);
	for (int i = c_size - M; i < c_size; i++) {
		selected[i] = 1;
	}
	
	do {
		int total_distance = 0;
		for (int i = 0; i < h_size; i++) {
			int distance = 1000;
			for (int j = 0; j < c_size; j++) {
				if (!selected[j]) continue;
				distance = min(distance, abs(house[i].first - chicken[j].first) + abs(house[i].second - chicken[j].second));
			}
			total_distance += distance;
		}
		ans = min(ans, total_distance);
	} while (next_permutation(selected.begin(), selected.end()));
	cout << ans;
}