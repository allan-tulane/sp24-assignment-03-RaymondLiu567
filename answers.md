# CMPS 2200 Assignment 3
## Answers

**Name:**__Raymond Liu_______________________


Place all written answers from `assignment-03.md` here for easier grading.

1a)
To convert an amount `N` into the least number of coins in Geometrica, we can use the following greedy algorithm:

1. Start with the highest denomination less than or equal to `N`. This will be `2^k` where `k` is the largest integer such that `2^k <= N`.
2. Use as many of these coins as possible without exceeding `N`. This will be `N // 2^k` coins of denomination `2^k`.
3. Subtract the total value of these coins from `N` to get the new remaining amount `N'`.
4. Repeat the process with the next lower denomination for `N'` until `N` is reduced to 0.
5. The result will be the list of coins that add up to `N` using the least number of coins.

1b)
The greedy algorithm is optimal for the coin system in Geometrica, which can be proven by showing the greedy choice and optimal substructure properties:

Greedy Choice Property: At each step, choosing the largest possible denomination that does not exceed the remaining amount N ensures that the number of coins used is minimized. This is because, by definition, no larger coin could be used, and any smaller coin would necessitate more coins to reach the same amount.

Optimal Substructure: The problem of making change for N using the largest coin 2^k can be broken down into making change for the remaining amount N - 2^k. The optimal solution for making change for N includes the optimal solution for making change for N - 2^k, plus the coin 2^k. This is because the subproblem (N - 2^k) is independent of the choice of the first coin and thus can be optimally solved without considering the initial greedy choice.

1c)
Work (W): The work of the algorithm is primarily the repeated division and modulus operations to find the largest denomination and the number of such coins to use. For denominations of powers of 2, this process involves O(log N) operations, since each coin reduces the problem size by a factor of 2.

Span (S): The span, which is the longest chain of dependent operations, is also O(log N). This is because each step of the algorithm depends on the completion of the previous step, as it requires the new reduced amount N' to proceed.

2a)
Consider the denominations of Fortuito are {1, 3, 4, 6}. Let's say we need to make change for N = 8 dollars.

- Greedy Algorithm: The greedy algorithm would choose the largest denomination less than or equal to 8, which is 6. Then it would choose two 1-dollar coins. In total, we get 3 coins.
- Optimal Solution: An optimal solution would use two 4-dollar coins, totaling only 2 coins.

This example shows that the greedy algorithm can lead to suboptimal solutions in Fortuito, as it does not always produce the fewest number of coins.

2b)
The coin change problem in Fortuito exhibits the optimal substructure property which is stated as follows:

- Property: The minimum number of coins required to change amount `N` with denominations `D` can be derived by taking the minimum number of coins required to make change for `N - d` for each denomination `d` in `D`, plus one additional coin of denomination `d`.

- Proof: Suppose we have an optimal solution for `N`. If we remove one coin of denomination `d` from this solution, the remaining coins must be an optimal solution for `N - d`. If there were a better solution for `N - d`, we could replace the current coins for `N - d` with this better solution and add the removed coin back, producing a better solution for `N` than we assumed, which is a contradiction. Therefore, the problem has the optimal substructure property.

2c)
To utilize the optimal substructure property, we can design a dynamic programming algorithm as follows:

- Define `dp[i]` as the minimum number of coins required to make change for amount `i`.
- Initialize `dp[0] = 0`, and for all other amounts, initialize `dp[i]` to a large number representing infinity (as we don't yet know the minimum coins required).
- For each amount `i` from `1` to `N` and for each denomination `d`, update `dp[i]` as `dp[i] = min(dp[i], dp[i - d] + 1)` if `i >= d`.
- The result `dp[N]` gives the minimum number of coins needed to make change for `N`.

- Work (W): The work done by this algorithm is `O(N * k)` since we iterate over all amounts up to `N` and check each of the `k` denominations for each amount.
- Span (S): The span of the algorithm is `O(N)` assuming that the update of `dp[i]` can be done in parallel for different `i`. However, if the updates must be done sequentially, the span could also be `O(N * k)`.