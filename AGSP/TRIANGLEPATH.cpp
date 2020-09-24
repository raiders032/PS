/*
 1.������ ������ �����Ѵ�.
 2.ĳ�� �ʱ�ȭ
 3.������� ó��
 4.ĳ���� �������� ��ȯ�Ѵ�.

 ������
 1.���� Ž������ Ǯ��
 2.�ߺ��Ǵ� ������ �޸������̼�
*/

#include<iostream>
#include<algorithm>
#include<string.h>

using namespace std;

int N;
int board[100][100];
int cache[100][100];

int solve(int x, int y) {
	if (x == N)
		return 0;
	int& result = cache[x][y];
	if (result != -1)
		return result;

	return result = (board[x][y] + max(solve(x + 1, y), solve(x + 1, y + 1)));
}

int main(void) {
	int testCase;
	cin >> testCase;
	while (testCase--) {
		cin >> N;
		memset(cache, -1, sizeof(cache));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j <= i; j++) {
				cin >> board[i][j];
			}
		}
		cout << solve(0, 0) << "\n";
	}
}