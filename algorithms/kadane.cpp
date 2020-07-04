#include <algorithm> // max function

using namespace std;

int maxSubarraySum(int n, int arr[]) {
    int curr_sum = arr[0], max_sum = arr[0];
    for (int i = 1; i < n; i++) {
        curr_sum = max(arr[i], curr_sum + arr[i]);
        max_sum = max(curr_sum, max_sum);
    }
    return max_sum;
}
