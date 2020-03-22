#include<iostream>
#include<vector>
#include<memory.h>

using namespace std;

bool visited[101];
vector <vector<int>> graph;

void dfs(int v) {
	visited[v] = true;
	for (int i = 0; i < graph[v].size(); i++) {
		if (!visited[graph[v][i]])
			dfs(graph[v][i]);
	}
}

int main(void) {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int N, M, ans = 0;
		cin >> N >> M;
		graph.resize(N+1);
		memset(visited, false, sizeof(visited));
		for (int i = 0; i < M; i++) {
			int u, v;
			cin >> u >> v;
			graph[u].push_back(v);
			graph[v].push_back(u);
		}
		for (int i = 1; i <= N; i++) {
			if (!visited[i]) {
				dfs(i);
				ans++;
			}
		}
		for (int i = 0; i <= N; i++)
			graph[i].clear();
		graph.clear();
		cout << "#" << tc << " " <<ans << "\n";
	}

}