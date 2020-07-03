#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

int n_jumpgame, board_jumpgame[100][100];
int cache_jumpgame[100][100];


int jump(int x, int y) {


	if (x >= n_jumpgame || y >= n_jumpgame)
		return 0;

	if (x < 0 || y < 0)
		return 0;

	// basis
	if (x == n_jumpgame -1 && y == n_jumpgame -1)
		return 1;


	int& ret = cache_jumpgame[x][y];

	if (ret != -1)
		return ret;

	int size = board_jumpgame[x][y];

	return ret = (jump(x + size, y) || jump(x, y + size));
	
}

int lec8_2() {
	int C;
	cin >> C;
	for (int case_num=0; case_num < C; case_num++) {
		cin >> n_jumpgame;
		memset(cache_jumpgame, -1, sizeof(cache_jumpgame));
		for (int i = 0; i < n_jumpgame; i++)
			for (int j = 0; j < n_jumpgame; j++) {
				cin >> board_jumpgame[i][j];
			}
		int test = jump(0, 0);

		if (test == 1)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}


	return 0;
}