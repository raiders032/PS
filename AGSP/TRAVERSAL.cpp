#include<iostream>
#include<vector>

using namespace std;

vector<int> slice(const vector<int>& v, int a, int b) {
	return vector<int>(v.begin() + a, v.begin() + b);
}

void printPostOrder(const vector<int>& preOrder, const vector<int>& inOrder) {
	int N = preOrder.size();
	if (N == 0)
		return;
	int root = preOrder[0];
	int L = find(inOrder.begin(), inOrder.end(), root) - inOrder.begin();
	int R = N - L -1;

	printPostOrder(slice(preOrder, 1, L+1), slice(inOrder,  0 ,L));
	printPostOrder(slice(preOrder, L + 1, N ), slice(inOrder, L + 1, N));
	cout << root << " ";
}

int main(void) {
	int testCase;
	cin >> testCase;
	while (testCase--) {
		int n;
		vector<int> preOrder;
		vector<int> inOrder;
		cin >> n;
		for (int i = 0; i < n; i++) {
			int tmp;
			cin >> tmp;
			preOrder.push_back(tmp);
		}
		for (int i = 0; i < n; i++) {
			int tmp;
			cin >> tmp;
			inOrder.push_back(tmp);
		}
		printPostOrder(preOrder, inOrder);
		cout << "\n";
	}
}