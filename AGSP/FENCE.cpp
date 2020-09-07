#include<iostream>
#include<algorithm>

using namespace std;

int N;
int fence[20000];

int solve(int left, int right) {
	//basecase
	if (left == right) {
		return fence[left];
	}

	//divide
	int mid = (left + right) / 2;
	int leftSize = solve(left, mid);
	int rightSize = solve(mid+1, right);

	//merge
	int minHeight = min(fence[mid], fence[mid + 1]);
	int middleSize = minHeight * 2;
	int l = mid;
	int r = mid + 1;
	while (left < l || r < right) {
		if ((fence[l - 1] <= fence[r + 1] || l == left) && r < right) {
			minHeight = min(minHeight, fence[++r]);
		}
		else {
			minHeight = min(minHeight, fence[--l]);
		}
		middleSize = max(middleSize, minHeight * (r - l + 1));
	}
	return max(middleSize, max(leftSize, rightSize));
}

int main(void) {
	int testCase;
	cin >> testCase;
	while (testCase--) {
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> fence[i];
		}
		cout << solve(0, N - 1) << "\n";
	}
}