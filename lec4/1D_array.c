//10818
#include <stdio.h>
#define CRT_SECURE_NO_WARNINGS

int main() {
	int N = 0;
	int input = 0;
	int m = 1000001, M = -1000001;

	// N ���� �Է� �ޱ�
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d", &input);

		// �ִ� ���ϱ�
		if (input > M) {
			M = input;
		}
		// �ּڰ� ���ϱ�
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
		// �ڿ��� �б�
		scanf("%d", &input);
		count++;

		// �ڿ����� 100���� �۴�
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
	// ���� ���� ������ ����
	char input[8] = { 0, };
	char* ascending = "12345678";
	char* descending = "87654321";

	// ���� �о���̱�
	for (int i = 0; i < 8; i++) {
		scanf("%s", &input[i]);
	}

	//������ ���غ���
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
