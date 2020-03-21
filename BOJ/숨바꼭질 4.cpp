#include<iostream>
#include<queue>
#include<memory.h>

using namespace std;

int visited[100001];
int pre[100001];
int N, K;

void bfs() {
	queue <int> q;
	int cur;
	visited[N] = 0;
	pre[N] = -1;
	q.push(N);
	while (!q.empty()) {
		cur = q.front();
		q.pop();

		if (cur == K) {
			vector <int> ans(visited[K]+1);
			int i = visited[K];
			cout << visited[K] << "\n";
			while (pre[cur] != -1) {
				ans[i--] = cur;
				cur = pre[cur];
			}
			ans[0] = N;
			for (int i = 0; i <= visited[K]; i++)
				cout << ans[i] << " ";
			return;
		}
		
		if (cur > 0) {
			if (visited[cur - 1] == -1) {
				visited[cur - 1] = visited[cur] + 1;
				pre[cur - 1] = cur;
				q.push(cur - 1);
			}
		}
		if (cur < 100000) {
			if (visited[cur + 1] == -1) {
				visited[cur + 1] = visited[cur] + 1;
				pre[cur + 1] = cur;
				q.push(cur + 1);
			}
		}
		if (2 * cur <= 100000) {
			if (visited[2 * cur] == -1) {
				visited[2 * cur] = visited[cur] + 1;
				pre[2 * cur] = cur;
				q.push(2 * cur);
			}
		}
	}
}

int main(void) {
	cin >> N >> K;
	memset(pre, -1, sizeof(pre));
	memset(visited, -1, sizeof(visited));
	bfs();
	return 0;
}