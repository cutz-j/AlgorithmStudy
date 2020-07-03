#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

int C_8_8, n_8_8;
int board_8_8[100][100];
int cache_8_8[100][100];

int search(int x, int y) {
	//basis
	if (y == n_8_8 - 1)
		return board_8_8[x][y];

	int& ret = cache_8_8[x][y];
	if (ret != -1)
		ret;

	return ret = max(search(x, y + 1), search(x + 1, y + 1)) + board_8_8[x][y];

}

int lec_8_8_triangle(void) {
	
	cin >> C_8_8;


	for (int case_num = 0; case_num < C_8_8; case_num++) {
		cin >> n_8_8;

		for (int i = 0; i < n_8_8; i++)
			for (int j = 0; j < i+1; j++) {
				cin >> board_8_8[i][j];
			}


		int res = search(0, 0);
		cout << res << endl;

	}


	return 0;
}