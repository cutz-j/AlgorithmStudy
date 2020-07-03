#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

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

bool align(const vector<int>& clocks);

void pushButton(vector<int>& clocks, int btn) {
	for (int c = 0; c < button[btn].size(); c++) {
		clocks[button[btn][c]] += 3;
		if (clocks[button[btn][c]] == 15)
			clocks[button[btn][c]] = 3;
	}
}

int solver(vector<int>& clocks, int btn) {
	if (btn == 10)
		return align(clocks) ? 0 : 987654321;
	int ret = 987654321;
	for (int c = 0; c < 4; c++) {
		ret = min(ret, c + solver(clocks, btn + 1));
		pushButton(clocks, btn);
	}
	return ret;
}

int main(void) {
	int C, n;
	vector<int> clocks;
	cin >> C;
	for (int i = 0; i < C; i++) {
		for (int j = 0; j < 16; j++) {
			cin >> n;
			clocks[j] = n;
		}

		solver(clocks, i);
	}
	
	clocks;
	solver();
	return 0;
}