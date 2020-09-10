/*
1. �ߺ��Ǵ� �κ� ������ ����
2. ������ ������ ����
3. ������ȹ�� �����ϱ�

�޸������̼� ��������
1. �׻� ���� ��� ���� ó��
2. cache �ʱ�ȭ
3. cache�� �������� ��ȯ
*/

#include<iostream>
#include<string.h>
using namespace std;

int N;
int cache[100][100];
int board[100][100];
int dx[2] = { 0,1 };
int dy[2] = { 1,0 };

int solve(int x, int y) {
	if (x >= N || y >= N)
		return 0;
	if (x == N - 1 && y == N - 1)
		return 1;
	int& ret = cache[x][y];
	if (ret != -1)	return ret;
	int distance = board[x][y];
	return ret = (solve(x + distance, y) || solve(x, y + distance));
}

int main(void) {
	int testCase;
	cin >> testCase;
	while (testCase--) {
		cin >> N;
		memset(cache, -1, sizeof(cache));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> board[i][j];
			}
		}
		if (solve(0, 0))
			cout << "YES";
		else
			cout << "NO";
		cout << "\n";
	}
}