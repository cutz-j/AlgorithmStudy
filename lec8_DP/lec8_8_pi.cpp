#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;


string N_pi;
int cache_pi[10001];

int classify(int a, int b) {
	string d = N_pi.substr(a, b-a+1);
	// case 1
	if (d == string(d.size(), d[0]))
		return 1;

	// case 2 // abs 1 increasing or decreasing
	bool case_2 = true;
	for (int i = 0; i < d.size() - 1; i++)
		if (d[i + 1] - d[i] != d[1] - d[0])
			case_2 = false;
	if (case_2 && abs(d[1] - d[0]) == 1)
		return 2;

	// case 3 // alternating
	bool case_3 = true;
	for (int i = 0; i < d.size(); i++)
		if (d[i] != d[i % 2])
			case_3 = false;
	if (case_3)
		return 4;

	// case 4 // (not 1) increasing or decreasing
	if (case_2)
		return 5;

	return 10;
}

int search(int start) {
	if (start == N_pi.size())
		return 0;

	int& ret = cache_pi[start];
	if (ret != -1)
		return ret;

	ret = 1e9;
	for (int i = 3; i <= 5; ++i) {
		if (start + i <= N_pi.size()) {
			ret = min(ret, search(start+i) + classify(start, start+i-1));
			
		}
	}

	cache_pi[start] = ret;
	return ret;



}

int main(void) {
	int C;
	cin >> C;
	for (int case_num = 0; case_num < C; case_num++) {
		memset(cache_pi, -1, sizeof(cache_pi));
		cin >> N_pi;
		cout << search(0) << endl;

	}
	
	return 0;
}