#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(void) {
	int sum = 0;
	int i, j;
	vector <int> arr(9);
	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
		sum += arr[i];
	}
	sum -= 100;
	sort(arr.begin(), arr.end());
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			if (i == j) continue;
			if (arr[i] + arr[j] == sum) {
				for (int k = 0; k < 9; k++) {
					if (k == i || k == j)continue;
					cout << arr[k] << "\n";
				}
				return 0;
			}
		}
	}
}