public class Solution {
    public int CountComponents(int n, int[][] edges) {
        var adjList = new List<int>[n];
        for (int i = 0; i < n; i++) adjList[i] = new List<int>();
        foreach (int[] edge in edges) {
            int n1 = edge[0], n2 = edge[1];
            adjList[n1].Add(n2);
            adjList[n2].Add(n1);
        }

        var visited = new HashSet<int>();
        void Dfs(int vert) {
            if (visited.Contains(vert)) return;

            visited.Add(vert);
            foreach (int connectedVert in adjList[vert]) Dfs(connectedVert);
        }

        int count = 0;
        for (int vert = 0; vert < n; vert++) {
            if (!visited.Contains(vert)) {
                count++;
                Dfs(vert);
            }
        }
        return count;
    }
}
