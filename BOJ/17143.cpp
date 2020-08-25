#include<iostream>
#include<vector>
#include<math.h>
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
vector <shark> shark_list;

void catch_shark(int col) {
	int idx;
	int dist = 200;
	int size = shark_list.size();
	for (int i = 0; i < size; i++) {
		if (shark_list[i].c != col) continue; 
		if (shark_list[i].r < dist) {
			idx = i;
			dist = shark_list[i].r;
		}
	}
	shark_list.erase(shark_list.begin() + idx);
}

void move_shark(shark shark) {
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
}

int main(void) {
	int r, c, s, d, z;
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
	for (int col = 1; col <= c; col++) {
		catch_shark(col);
		move();
	}
}