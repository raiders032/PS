#include<iostream>
#include<vector>

using namespace std;

vector <vector<int>> switchs(10);

int pushSwitch(int x) {
	switchs[0].push_back(0);

}

int main(void) {
	int tc;
	vector <int> clocks(16);
	vector <int> visited(16, 0);
	cin >> tc;

	while (tc--) {
		for (int i = 0; i < 16; i++)
			cin >> clocks[i];
		fill(visited.begin(), visited.end(), 0);
		cout << pushSwitch(0)<<"\n";
	}
}










