/*
1. 중복되는 부분 문제가 존재
2. 참조적 투명성을 만족
3. 동적계획법 적용하기

메모이제이션 구현패턴
1. 항상 기저 사례 먼저 처리
2. cache 초기화
3. cache의 참조형을 반환
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