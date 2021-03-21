#include<iostream>
#include<string>
#include<math.h>
#include<algorithm>

using namespace std;

int main(void) {
	int N;
	int sum[26];
	cin >> N;
	for (int i = 0; i < 26; i++)
		sum[i] = 0;
	while (N--) {
		string str;
		cin >> str;
		for (int i = 0; i < str.size(); i++) {
			sum[str[i] - 'A'] += pow(10, str.size() - i - 1);
		}
	}
	sort(sum, sum + 26);
	int ans = 0;
	int j = 25;
	for (int i = 9; i > 0; i--) {
		ans += sum[j--] * i;
	}
	cout << ans;
}