#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;
vector<int> a;

bool judge(int m) {
    bool dp[5010] = {false};
    dp[0] = true;
    for (auto i = 0; i < N; i++) {
        if (i == m) continue;
        for (auto j = K-a[i]-1; j >= 0; j--) {
            if (!dp[j]) continue;
            if (K-a[m] <= j+a[i]) {
                return true;
            }
            dp[j+a[i]] = true;
        }
    }
    return false;
}

int main() {
    int x;
    
    cin >> N >> K;
    for (auto i = 0; i < N; i++) {
        cin >> x;
        if (x < K) {
            a.push_back(x);
        }
    }
    sort(a.begin(), a.end());
    
    N = a.size();
    int l, r, m;
    l = -1;
    r = N;
    while (r - l > 1) {
        m = (l + r) / 2;
        if (judge(m)) {
            r = m;
        } else {
            l = m;
        }
    }
    cout << r << endl;
	return 0;
}