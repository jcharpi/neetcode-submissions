class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for node_count in range(2, n + 1):
            for root in range(1, node_count + 1):
                # Trees with this root = (left subtree options) * (right subtree options)
                left_subtree_size = root - 1
                right_subtree_size = node_count - root
                dp[node_count] += dp[left_subtree_size] * dp[right_subtree_size]

        return dp[n]