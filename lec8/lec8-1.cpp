#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int cache[30][30];
int call_num;


int bino_dp(int n, int r) {
	call_num += 1;
	if (n == r || r == 0)
		return 1;
	if (cache[n][r] != -1)
		return cache[n][r];
	return cache[n][r] = bino_dp(n - 1, r - 1) + bino_dp(n - 1, r);
}

int lec8_1() {
	for (int i = 0; i < 30; i++)
		fill_n(cache[i], 30, -1);
	int test = bino_dp(25, 12);
	cout << test << ' ' << call_num;

	return 0;
}