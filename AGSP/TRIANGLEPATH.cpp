/*
 1. ������ ������ �����ϴ°�? yes
 2. ���� ��ȹ���� ��������.
 3. cache �ʱ�ȭ
 4. ������� ó��
 5. cache�� ������ ��ȯ
*/
#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

int cache[100][100];
int board[100][100];
int N;

int solve(int r, int c) {
	if (r == N - 1 ) return board[r][c];
	int& result = cache[r][c];
	if (result != -1) return result;
	return result = board[r][c] + max(solve(r + 1, c), solve(r + 1, c + 1));
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
		cout<<solve(0, 0)<<"\n";
	}
}