public class Solution {
    public int MinCostConnectPoints(int[][] points) {
        int n = points.Length;
        int GetCost(int src, int dest) {
            int srcX = points[src][0], destX = points[dest][0];
            int srcY = points[src][1], destY = points[dest][1];
            return Math.Abs(srcX - destX) + Math.Abs(srcY - destY);
        }

        Dictionary<int, List<(int dest, int cost)>> adjList = new();
        for (int i = 0; i < n; i++) adjList[i] = new List<(int dest, int cost)>();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int dist = GetCost(i, j);
                adjList[i].Add((j, dist));
                adjList[j].Add((i, dist));
            }
        }

        int minCost = 0;
        PriorityQueue<(int src, int dest), int> minHeap = new();
        HashSet<int> visited = new();
        foreach ((int dest, int cost) in adjList[0]) minHeap.Enqueue((0, dest), cost);
        
        visited.Add(0);
        while (minHeap.TryDequeue(out (int src, int dest) edge, out int cost)) {
            if (visited.Contains(edge.dest)) continue;
            visited.Add(edge.dest);
            minCost += cost;

            foreach ((int nextDest, int nextCost) in adjList[edge.dest]) {
                if (!visited.Contains(nextDest)) minHeap.Enqueue((edge.dest, nextDest), nextCost);
            }
        }
        return minCost;
    }
}
