#include<iostream>
#include<cstdio>
#include<math.h>
#include<deque>

using namespace std;

deque <int> gear[4];

void rotate(int idx, int dir) {
	if (dir == 1) {
		gear[idx].push_front(gear[idx].back());
		gear[idx].pop_back();
	}
	else if(dir == -1) {
		gear[idx].push_back(gear[idx].front());
		gear[idx].pop_front();
	}
}

int main(void) {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 8; j++) {
			int tmp;
			scanf("%1d", &tmp);
			gear[i].push_back(tmp);
		}
	}

	int K, idx, d, ans = 0;
	int dir[4] = { 0,0,0,0 };
	cin >> K;
	for (int i = 0; i < K; i++) {
		cin >> idx >> d;
		dir[--idx] = d;
		for (int j = idx; j < 3; j++) {
			if (gear[j][2] == gear[j + 1][6])
				break;
			dir[j + 1] = -1 * dir[j];
		}
		for (int j = idx; j > 0; j--) {
			if (gear[j][6] == gear[j - 1][2])
				break;
			dir[j - 1] = -1 * dir[j];
		}
		for (int j = 0; j < 4; j++) {
			rotate(j, dir[j]);
			dir[j] = 0;
		}
	}

	for (int i = 0; i < 4; i++) {
		ans += gear[i][0] * pow(2, i);
	}
	cout << ans;
}