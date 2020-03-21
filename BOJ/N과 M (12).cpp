#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N, M;
vector <int> arr;
vector <int> visited;

void dfs(int cnt, int idx) {
	if (cnt == M) {
		for (int i = 0; i < visited.size(); i++) {
			cout << visited[i] << " ";
		}
		cout << "\n";
		return;
	}
	for (int i = idx; i < arr.size(); i++) {
		visited.push_back(arr[i]);
		dfs(cnt + 1, i);
		visited.pop_back();
	}
}

int main(void) {
	cin >> N >> M;
	arr.resize(N);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	sort(arr.begin(), arr.end());
	arr.erase(unique(arr.begin(), arr.end()), arr.end());
	dfs(0, 0);
}