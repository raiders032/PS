#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

struct Fish {
	int num = 0;
	int dir = 0;
	bool isDead = false;
	Fish(){
	
	}
	Fish(int Num, int Dir, bool IsDead) :num(Num), dir(Dir), isDead(IsDead) {

	}
};
struct Shark {
	int dir = 0;
	int cnt = 0;
	int x;
	int y;
};
int dx[9] = { 0,-1,-1,0,1,1,1,0,-1 };
int dy[9] = { 0,0,-1,-1,-1,0,1,1,1 };

Fish fish[4][4];
Shark shark;

bool findPos(int num, int& x, int& y) {
	bool find = false;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (fish[i][j].num == num) {
				x = i;
				y = j;
				find = true;
				break;
			}
		}
	}
	return find;
}

void moveFish() {
	for (int num = 1; num <= 16; num++) {
		int x, y;
		if (!findPos(num, x, y)) continue;
		if (fish[x][y].isDead) continue;
		for (int dir = fish[x][y].dir, i = 0; i < 8; i++, dir = (dir == 8 ? 1: dir +1 )) {
			int nx = x + dx[dir];
			int ny = y + dy[dir];
			if (nx < 0 || nx >= 4 || ny < 0 || ny >= 4)	continue;
			if (shark.x == nx && shark.y == ny) continue;
			swap(fish[x][y], fish[nx][ny]);
			break;
		}
	}
}

void copy(Fish source[][4], Fish destination[][4]) {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			destination[i][j] = source[i][j];
		}
	}
}

bool moveShark(Fish fish[][4]) {
	bool canEat = false;
	int nx = shark.x;
	int ny = shark.y;
	while(true){
		nx += dx[shark.dir];
		ny += dy[shark.dir];
		Fish tempFish[4][4];
		Shark tempShark;
		memcpy(tempFish, fish, sizeof(tempFish));
		if (nx < 0 || nx >= 4 || ny < 0 || ny >= 4)	break;
		if (tempFish[nx][ny].isDead) continue;
		shark.x = nx;
		shark.y = ny;
		shark.dir = tempFish[nx][ny].dir;
		tempFish[nx][ny].isDead = true;

	}
	return canEat;
}

int main(void) {
	int n, d;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (i == 0 && j == 0) {
				cin >> n >> d;
				shark = { d, 0, 0, 0 };
				fish[i][j] = Fish(0, 0, true);
			}
			else {
				cin >> n >> d;
				fish[i][j] = Fish(n, d, false);
			}
			
		}	
	}

	while (true) {
		moveFish();
		moveShark(fish);
	}
	
	return 0;
}