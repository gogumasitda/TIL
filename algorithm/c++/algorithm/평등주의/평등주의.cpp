// x���� >= 49�� ������? yes or no�� ����� �� �ְ� ���� ��ȯ
// yes�� ���� ���� ���� �̺�Ž���� ���ؼ� ���� ���� �ָ� ã�´�.
// �Ķ��Ʈ�� ��ġ

#include <iostream>
using namespace std;

int T, N, K, arr[100000], ans;

bool check(int W) {

}

void binarySearch(int left, int right) {
	int mid;
	ans = left;
	while (left <= right) {
		mid = (left + right) / 2;
		if (check(mid)) {
			ans = mid;
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}
	return;
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &arr[i]);
		}
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}

// ������ ���ڸ� x���Ϸ�