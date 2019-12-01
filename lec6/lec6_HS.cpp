#include <iostream>

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

int main(void) {
	const string word = "YES";
	if(hasWord(2, 2, word))
		cout << "found" << endl;

	return 0;
}