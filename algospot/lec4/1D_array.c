//10818
#include <stdio.h>
#define CRT_SECURE_NO_WARNINGS

int main() {
	int N = 0;
	int input = 0;
	int m = 1000001, M = -1000001;

	// N 정수 입력 받기
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d", &input);

		// 최댓값 구하기
		if (input > M) {
			M = input;
		}
		// 최솟값 구하기
		if (input < m) {
			m = input;
		}
	}

	printf("%d %d", m, M);
}

//2562
#include <stdio.h>
#define CRT_SECURE_NO_WARNINGS

int main() {
	int M = 0;
	int input = 0;
	int n = 0;
	int count = 0;

	for (int i = 1; i < 10; i++) {
		// 자연수 읽기
		scanf("%d", &input);
		count++;

		// 자연수는 100보다 작다
		if (0 < input && input < 100) {
			if (M < input) {
				M = input;
				n = count;
			}
		}
	}

	printf("%d\n", M);
	printf("%d", n);
}

//2920
#include <stdio.h>
#define CRT_SECURE_NO_WARNINGS

int main() {
	// 음계 순서 저장할 변수
	char input[8] = { 0, };
	char* ascending = "12345678";
	char* descending = "87654321";

	// 음계 읽어들이기
	for (int i = 0; i < 8; i++) {
		scanf("%s", &input[i]);
	}

	//각각과 비교해보기
	if (strcmp(input, ascending) == 0) {
		printf("ascending");
	}
	else if (strcmp(input, descending) == 0) {
		printf("descending");
	}
	else {
		printf("mixed");
	}
}
