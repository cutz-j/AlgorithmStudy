#include <iostream>

int q10818(void) {
	int N;
	int num;
	int min = 9999999;
	int max = -9999999;
	std::cin >> N;
	int *arr = new int[N];
	for (int i = 0; i < N; i++) {
		std::cin >> num;
		arr[i] = num;
		if (num > max) {
			max = arr[i];
		}
		if (num < min) {
			min = arr[i];
		}
	}
	
	std::cout << min << " " << max;
			
	return 0;
}

int q2562(void) {
	int N = 9;
	int num;
	int seq;
	int max=0;

	for (int i = 0; i < N; i++) {
		std::cin >> num;
		if (num > max) {
			max = num;
			seq = i + 1;
		}
	}
	
	std::cout << max << std::endl << seq;
		
	return 0;
}

int q2920(void) {
	int sw = 0;
	int m = 0;
	int num;
	int before;
	std::cin >> num;
	before = num;
	for (int i = 0; i < 7; i++) {
		std::cin >> num;
		if (before - num == 1)
			sw = -1;
		else if (before - num == -1)
			sw = 1;
		else
			m = 1;
		before = num;
	}

	if (m == 1) {
		std::cout << "mixed";
		return 0;
	}
	if (sw == -1) {
		std::cout << "descending";
		return 0;
	}
	if (sw == 1) {
		std::cout << "ascending";
		return 0;
	}
	return 0;
}

int main(void) {
	//q10818();
	//q2562();
	q2920();

	return 0;
}

