#include <stdio.h>
#include <math.h>
#define _CRT_SECURE_NO_WARNINGS

#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
typedef long long ll;

const int INF = 987654321;

//A[]: ����ȭ���� �� ����, ���ĵ�
//pSum[]: A[]�� �κ����� �����Ѵ�. pSum[i]�� A[0]...A[i]�� ��
//pSqSum[]: A[]������ �κ����� �����Ѵ�. pSqSum[i]�� A[0]^2...A[i]^2�� ��
int n;
int A[101], pSum[101], pSqSum[101];

//A�� �����ϰ� �� �κ����� ����Ѵ�
void precalc() {
	sort(A, A + n);
	pSum[0] = A[0];
	pSqSum[0] = A[0] * A[0];

	for (int i = 1; i < n; i++) {
		pSum[i] = pSum[i - 1] + A[i];
		pSqSum[i] = pSqSum[i - 1] + A[i] * A[i];
	}
}

//A[lo]...A[hi] ������ �ϳ��� ���ڷ� ǥ���� �� �ּ� ���� ���� ����Ѵ�
int minError(int lo, int hi) {
	//�κ����� �̿��� A[lo]...A[hi]������ ���� ���Ѵ�
	int sum = pSum[hi] - (lo == 0 ? 0 : pSum[lo - 1]);
	int sqSum = pSqSum[hi] - (lo == 0 ? 0 : pSqSum[lo - 1]);

	//����� �ݿø��� ������ �� ������ ǥ���Ѵ�
	int m = (int)(0.5 + (double)sum / (hi - lo + 1));

	//sum (A[i]-m)^2�� ������ ����� �κ� ������ ǥ��
	int ret = sqSum - 2 * m * sum + m * m * (hi - lo + 1);
	
	return ret;
}

int cache[101][11];
int quantize(int from, int parts) {
	//�������: ��� ���ڸ� �� ����ȭ ���� ��
	if (from == n) return 0;
	
	//�������: ���ڴ� ���� ���Ҵµ� �� ���� �� ���� �� ���� ū ���� ��ȯ�Ѵ�
	if (parts == 0) return INF;
	int ret = &cache[from][parts];
	if (ret != -1) return ret;
	ret = INF;

	//������ ���̸� ��ȭ���� ���� �ּ�ġ�� ã�´�
	for (int partSize = 1; from + partSize <= n; ++partSize) {
		ret = min(ret, minError(from, from + partSize - 1)) + quantize(from + partSize, parts - 1);
	}
	return ret;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	REP(cc, cases)
	{
		int parts;
		scanf("%d %d", &n, &parts);
		REP(i, n) scanf("%d", &A[i]);

		precalc();
		memset(cache, -1, sizeof(cache));
		printf("%d", quantize(0, parts));
	}
}
