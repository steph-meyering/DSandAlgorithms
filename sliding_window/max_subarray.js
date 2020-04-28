// Maximum Sum Subarray of Size K (easy)

// Given an array of positive numbers and a positive number ‘k’, find the 
// maximum sum of any contiguous subarray of size ‘k’.

// Example 1:

// Input: [2, 1, 5, 1, 3, 2], k=3 
// Output: 9
// Explanation: Subarray with maximum sum is [5, 1, 3].

// Example 2:

// Input: [2, 3, 4, 1, 5], k=2 
// Output: 7
// Explanation: Subarray with maximum sum is [3, 4].


const max_sub_array_of_size_k = function (k, arr) {
  let max = 0; // assumes numbers in arr are positive
  let winstart = 0;
  let winsum = 0;
  for (let winend = 0; winend < arr.length; winend++) {
    winsum += arr[winend];
    if (winend - winstart >= k - 1) { // check if window contains k elements
      if (winsum >= max) { // check if current window sum is greater than max
        max = winsum; // update max
      }
      winsum -= arr[winstart]; // subtract the first entry from the window
      winstart++; // slide window forward
    }
  }
  return max;
};


// Time complexity is linear
// Space complexity is constant