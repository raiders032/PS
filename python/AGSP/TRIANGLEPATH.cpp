/*
 1.참조적 투명성을 만족한다.
 2.캐시 초기화
 3.기저사례 처리
 4.캐시의 참조형을 반환한다.

 레시피
 1.완전 탐색으로 풀이
 2.중복되는 문제를 메모이제이션
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