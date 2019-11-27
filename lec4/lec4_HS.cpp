#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


vector<double> c4_3(const vector<double>& A, int M) {
	vector<double> ret;
	int N = A.size();
	for (int i = M - 1; i < N; ++i) {
		double partialSum = 0;
		for (int j = 0; j < M; ++j)
			partialSum += A[i - j];
		ret.push_back(partialSum / M);
	}
	return ret;
}

vector<double> c4_4(const vector<double>& A, int M) {
	
	vector<double> ret;
	double partialSum = 0;
	int N = A.size();
	for (int i = 0; i < M-1; i++)
		partialSum += A[i];
	for (int i = M - 1; i < N; i++) {
		partialSum += A[i];
		ret.push_back(partialSum / M);
		partialSum -= A[i - M + 1];
	}
	return ret;
	
}

//int selectMenu(vector<int>& menu, int food) {
//	const int INF = 987654321;
//	int M = 0;
//	bool canEverybodyEat(const vector<int> & menu);
//	if (food == M) {
//		if (canEverybodyEat(menu)) return menu.size();
//		return INF;
//	}
//	int ret = selectMenu(menu, food + 1);
//	menu.push_back(food);
//	ret = min(ret, selectMenu(menu, food + 1));
//	menu.pop_back();
//	return ret;
//}


const int MIN = numeric_limits<int>::min();

int inefficientMaxSum(const vector<int>& A) {
	int N = A.size(), ret = MIN;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			int sum = 0;
			for (int k = i; k <= j; ++k) {
				sum += A[k];
			}
			ret = max(ret, sum);
		}
	}
	return ret;
}

int betterMaxSum(const vector<int>& A) {
	int N = A.size(), ret = MIN;
	for (int i = 0; i < N; ++i) {
		int sum = 0;
		for (int j = i; j < N; ++j) {
			sum += A[j];
			ret = max(ret, sum);
		}
	}
	return ret;
}

int divideMaxSum(const vector<int>& A, int lo, int hi) {
	if (lo == hi) 
		return A[lo];

	int mid = (lo + hi) / 2;
	int left = MIN;
	int right = MIN;
	int sum = 0;

	for (int i = mid; i >= lo; --i) {
		sum += A[i];
		left = max(left, sum);
	}

	sum = 0;
	for (int j = mid + 1; j <= hi; ++j) {
		sum += A[j];
		right = max(right, sum);
	}
	int single = max(divideMaxSum(A, lo, mid), divideMaxSum(A, mid + 1, hi));
	return max(left + right, single);
}

int dynamicMaxSum(const vector<int>& A) {
	int N = A.size();
	int ret = MIN;
	int psum = 0;
	for (int i = 0; i < N; ++i) {
		psum = max(psum, 0) + A[i];
		ret = max(psum, ret);
	}
	return ret;
}

int q10818(void) {
	int N, num;
	cin >> N;
	int* arr = new int[N];
	int max = -987654321, min =  987654321;
	for (int i = 0; i < N; i++) {
		cin >> num;
		arr[i] = num;
	}
	for (int i = 0; i < N; i++) {
		if (max <= arr[i])
			max = arr[i];

		if (min >= arr[i])
			min = arr[i];
	}

	printf("%d %d", min, max);
	return 0;
}



int q3052(void) {
	int N, lf;
	int res = 0;
	int arr[42];
	for (int i = 0; i < 42; i++) {
		arr[i] = 0;
	}

	for (int i = 0; i < 10; i++) {
		cin >> N;
		lf = N % 42;
		arr[lf] = 1;
	}

	for (int i = 0; i < 42; i++) {
		res += arr[i];
	}
	cout << res;
	return 1;
}

int q1546(void) {
	int N, num;
	cin >> N;
	int* arr = new int[N];
	int max = -987654321;
	int idx = 0;
	int allsum = 0;
	
	for (int i = 0; i < N; i++) {
		cin >> num;
		arr[i] = num;
	}

	for (int i = 0; i < N; i++) {
		if (arr[i] >= max) {
			max = arr[i];
		}
	}

	for (int i = 0; i < N; i++) {
		idx = arr[i] / max * 100;
		allsum += idx;
	}


	cout << allsum/N;


	return 0;
}

int main(void) {
	//q10818();
	//q3052();
	q1546();
	return 0;
}
