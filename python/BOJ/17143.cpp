#include<iostream>
#include<vector>
#include<math.h>
#include<string.h>
using namespace std;

typedef struct _shark {
	int r;
	int c;
	int s;
	int d;
	int z;
}shark;

int board[101][101];
int R, C, M;
int dx[5] = {0,-1,1,0,0};
int dy[5] = {0,0,0,1,-1};
int ans = 0;
vector <shark> shark_list;

void catch_shark(int col) {
	int idx = -1;
	int dist = 200;
	int size = shark_list.size();
	for (int i = 0; i < size; i++) {
		if (shark_list[i].c != col) continue; 
		if (shark_list[i].r < dist) {
			idx = i;
			dist = shark_list[i].r;
		}
	}
	if (idx != -1) {
		ans += shark_list[idx].z;
		shark_list.erase(shark_list.begin() + idx);
	}
}

void move_shark(shark & shark) {
	int nr, nc, s= shark.s;
	switch (shark.d){
	case 1:
	case 2:
		while (s) {
			nr = shark.r + dx[shark.d];
			if (0 >= nr) {
				shark.d = 2;
				nr = shark.r + dx[shark.d];
			}
			else if (nr > R) {
				shark.d = 1;
				nr = shark.r + dx[shark.d];
			}
			shark.r = nr;
			s--;
		}	
		break;
	case 3:
	case 4:
		while (s) {
			nc = shark.c + dy[shark.d];
			if (0 >= nc) {
				shark.d = 3;
				nc = shark.c + dy[shark.d];
			}
			else if (nc > C) {
				shark.d = 4;
				nc = shark.c + dy[shark.d];
			}
			shark.c = nc;
			s--;
		}
		break;
	}
}

void move() {
	int size = shark_list.size();
	for (int i = 0; i < size; i++) {
		move_shark(shark_list[i]);
	}

	memset(board, -1, sizeof(board));

	for (int i = 0; i < shark_list.size(); i++) {
		int r = shark_list[i].r;
		int c = shark_list[i].c;
		if (board[r][c] == -1)
			board[r][c] = i;
		else {
			if (shark_list[board[r][c]].z < shark_list[i].z) {
				shark_list.erase(shark_list.begin() + board[r][c]);
				board[r][c] = --i;
			}
			else {
				shark_list.erase(shark_list.begin() + i--);
			}
		}
	}

}

int main(void) {
	int r, c, s, d, z, tmp;
	cin >> R >> C >> M;

	for (int i = 0; i < M; i++) {
		cin >> r >> c >> s >> d >> z;
		switch (d)
		{
		case 1:
		case 2:
			s = s % ((r - 1) + (R - 1) + (R - r));
			break;
		case 3:
		case 4:
			s = s % ((c - 1) + (C - 1) + (C - c));
			break;
		}
		shark_list.push_back({ r,c,s,d,z });
	}

	for (int col = 1; col <= C; col++) {
		catch_shark(col);
		move();
	}

	cout << ans;
}


/*
3 3 9
1 1 1000 1 1
1 2 999 2 2
2 1 1000 3 3
2 2 999 4 4
1 3 1000 1 5
3 1 999 2 6
2 3 1000 3 7
3 2 999 4 8
3 3 1000 1 9
정답 : 8
*/

/*
4 2 2
2 2 3 1 1
4 2 3 1 2
정답 : 2
*/

/*
10 10 2
1 9 8 2 1
5 10 7 4 2
정답 : 0 
*/

/*
100 3 2
2 3 0 1 2
4 3 1 1 3
정답 : 3
*/

/*
100 7 7
3 2 2 3 9
3 3 1 3 3
3 5 1 4 7
3 6 2 4 6
2 4 1 2 8
1 4 2 2 4
4 4 1 1 5
정답 : 0
*/