#include<iostream>
#include<vector>

using namespace std;

vector <int> slice(const vector<int>& v, int a, int b) {
	return vector<int>(v.begin() + a, v.begin() + b);
}

void printPost(const vector<int>& pre, const vector<int>& in) {
	int N = pre.size();
	if (N == 0)
		return;
	int root = pre[0];
	int L = find(in.begin(), in.end(), root) - in.begin();
	int R = N - L - 1;

	printPost(slice(pre,1,L + 1),slice(in, 0, L));
	printPost(slice(pre, L+1, N), slice(in, L + 1, N));
	cout << root << " ";
}

int main(void) {
	int N;
	int testCase;
	cin >> testCase;
	while (testCase--) {
		cin >> N;
		vector<int> pre(N);
		vector<int> in(N);
		for (int i = 0; i < N; i++)
			cin >> pre[i];
		for (int i = 0; i < N; i++)
			cin >> in[i];
		printPost(pre, in);
		cout << "\n";
	}
}