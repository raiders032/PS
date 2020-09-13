/*
 1. 참조적 투명성을 만족하는가? yes
 2. 동적 계획법을 적용하자.
 3. cache 초기화
 4. 기저사례 처리
 5. cache의 참조형 반환
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