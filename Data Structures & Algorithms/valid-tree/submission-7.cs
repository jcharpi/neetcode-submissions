public class Solution {
    public bool ValidTree(int n, int[][] edges) {
        if (edges.Length != n - 1) return false;

        List<int>[] adjList = new List<int>[n];
        for (int i = 0; i < n; i++) adjList[i] = new List<int>();

        foreach (int[] edge in edges) {
            adjList[edge[0]].Add(edge[1]);
            adjList[edge[1]].Add(edge[0]);
        }

        HashSet<int> visited = new HashSet<int>();
        bool Dfs(int node, int parent) {
            if (visited.Contains(node)) return false;

            visited.Add(node);
            foreach (int neighbor in adjList[node]) {
                if (neighbor == parent) continue;
                if (!Dfs(neighbor, node)) return false;
            }

            return true;
        }

        return Dfs(0, -1) && visited.Count == n;
    }
}
