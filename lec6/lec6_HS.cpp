#include <iostream>
#include <vector>

using namespace std;

const char BOARD[5][5] = { {'N', 'N', 'N', 'N', 'S'},
						  {'N', 'E', 'E', 'E', 'N'},
						  {'N', 'E', 'Y', 'E', 'N'},
						  {'N', 'E', 'E', 'E', 'N'},
						  {'N', 'N', 'N', 'N', 'N'} };

bool hasWord(int x, int y, const string& word) {
	int dx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };
	int dy[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
	
	if (x > 5 || x < 0)
		return false;
	if (y > 5 || y < 0)
		return false;
	if (BOARD[x][y] != word[0])
		return false;
	if (word.size() == 1)
		return true;

	for (int d = 0; d < 8; d++) {
		int next_x = x + dx[d];
		int next_y = y + dy[d];
		if (hasWord(next_x, next_y, word.substr(1)))
			return true;
	}

	return false;
}

int q6_3(void) {
	int C, N, S;
	cin >> C;
	int* res = new int[C];

	int f_num1, f_num2;
	bool friends[10][10];

	for (int i = 0; i < C; i++) {
		cin >> N >> S;
		bool taken[10];
		for (int j = 0; j < C; j++) {
			std::cin >> f_num1 >> f_num2;
			friends[f_num1][f_num2] = friends[f_num2][f_num1] = true;
		}
		



	}


	return 0;
}

int solver(bool taken[10], bool friends[10][10], int n) {
	
	bool finish = true;

	for (int i = 0; i < n; i++) {
		if (!taken[n])
			finish = false;
	}

	if (finish)
		return 1;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!taken[i] && !taken[j] && friends[i][j])
				taken[i] = taken[j] = true;
		}

	}
	return 0;
}

int solver_2(bool taken[10], bool friends[10][10], int n) {
	int first = -1;
	for (int i = 0; i < n; i++) {
		if (!taken[i]) {
			first = i;
			break;
		}
	}
	
	if (first == -1)
		return 1;
	int ret = 0;

	for (int pair = first + 1; pair < n; pair++) {
		if (!taken[pair] && friends[first][pair]) {
			taken[first] = taken[pair] = true;
			ret += solver_2(taken, friends, n);
			taken[first] = taken[pair] = false;
		}
	}
	return ret;
}

vector<vector<int> > button({
	vector<int>({ 0, 1, 2 }),
	vector<int>({ 3, 7, 9, 11 }),
	vector<int>({ 4, 10, 14, 15 }),
	vector<int>({ 0, 4, 5, 6, 7 }),
	vector<int>({ 6, 7, 8, 10, 12 }),
	vector<int>({ 0, 2, 14, 15 }),
	vector<int>({ 3, 14, 15 }),
	vector<int>({ 4, 5, 7, 14, 15 }),
	vector<int>({ 1, 2, 3, 4, 5 }),
	vector<int>({ 3, 4, 5, 9, 13 })
	});

int q6_8(void) {
	int C;
	cout << button[0][1];

	return 0;
}

int lec6(void) {
	q6_8();
	return 0;
}