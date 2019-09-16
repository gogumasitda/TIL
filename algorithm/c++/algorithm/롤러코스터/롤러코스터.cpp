#include <iostream>
using namespace std;

int T, N, visited[200001] = { 0, };
long long a, b, arr[200001][2], minNum;

// ��ȭ���� �̿��ؼ� Ǯ��ȴ�.
// �׸��� ���� ����� �� �� ���� �ַ� ����ϸ� ��.

void dfs(int depth, long long v) {
	if (depth == N) {
		if (minNum == 0) {
			minNum = v;
		}
		else if (v < minNum) {
			minNum = v;
		}
		return;
	}
	if (minNum != 0 && minNum <= v) {
		return;
	}
	for (int i = 0; i < N; ++i) {
		if (visited[i] == 1) {
			continue;
		}
		visited[i] = 1;
		dfs(depth + 1, arr[i][0] * v + arr[i][1]);
		visited[i] = 0;
	}
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		minNum = 0;
		scanf("%d", &N);
		for (int n = 0; n < N; ++n) {
			scanf("%ld %ld", &a, &b);
			arr[n][0] = a;
			arr[n][1] = b;
		}
		dfs(0, 1);
		printf("#%d %ld\n", tc, minNum % 1000000007);
	}
	return 0;
}