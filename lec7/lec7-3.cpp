#include<iostream>
#include<vector>
#include<algorithm>


using namespace std;

void addTo(vector<int>& a, const vector<int>& b, int k);
void subFrom(vector<int>& a, const vector<int>& b);

void normalize(vector<int>& num) {
	num.push_back(0);

	for (int i = 0; i + 1 < num.size(); i++) {
		if (num[i] < 0) {
			int borrow = (abs(num[i]) + 9) / 10;
			num[i + 1] -= borrow;
			num[i] += borrow * 10;
		}
		else {
			num[i + 1] += num[i] / 10;
			num[i] %= 10;
		}
	}
	while (num.size() > 1 && num.back() == 0)
		num.pop_back();
}

vector<int> multiply(const vector<int>& a, const vector<int> b) {
	vector<int> c(a.size() + b.size() + 1, 0);
	for (int i = 0; i < a.size(); i++)
		for (int j = 0; j < b.size(); j++) {
			c[i + j] += a[i] * b[j];
		}
	normalize(c);
	return c;
}


vector<int> karatsuba(const vector<int>& a, const vector<int>& b) {
	int an = a.size(), bn = b.size();
	if (an < bn)
		return karatsuba(b, a); // 무조건 a가 b보다 size가 길어야 한다.
	if (an == 0 || bn == 0)
		return vector<int>(); // a와 b가 빈 경우;
	if (an <= 50)
		return multiply(a, b);
	
	int half = an / 2;
	vector<int> a0(a.begin(), a.begin() + half);
	vector<int> a1(a.begin() + half, a.end());
	vector<int> b0(b.begin(), b.begin() + min<int>(b.size(), half));
	vector<int> b1(b.begin() + min<int>(b.size(), half), b.end());

	vector<int> z2 = karatsuba(a1, b1);
	vector<int> z0 = karatsuba(a0, b0);
	addTo(a0, a1, 0);
	addTo(b0, b1, 0);
	vector<int> z1 = karatsuba(a0, b0);
	subFrom(z1, z0);
	subFrom(z1, z2);
	vector <int> ret;
	addTo(ret, z0, 0);
	addTo(ret, z1, half);
	addTo(ret, z2, half + half);
	return ret;
}

void addTo(vector<int>& a, const vector<int>& b, int k) {
	a.resize(max((a.size() + 1), (b.size() + k)));

	for (int i = 0; i < b.size(); i++) {
		a[i + k] += b[i];
	}
	normalize(a);
}

void subFrom(vector<int>& a, const vector<int>& b) {
	for (int i = 0; i < b.size(); i++) {
		a[i] -= b[i];
	}
	normalize(a);
}


int main() {
	vector<int> a;
	vector<int> b;

	a.push_back(3);
	a.push_back(2);
	a.push_back(1);
	b.push_back(6);
	b.push_back(5);
	b.push_back(4);

	vector<int> ret = karatsuba(a, b);

	for (int i = 0; i < ret.size(); i++)
		cout << ret[i];

	return 0;
}

