public class Solution {
    public double MaxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        Dictionary<int, List<(int, double)>> adjList = new();
        for (int i = 0; i < n; i++) adjList[i] = [];
        for (int i = 0; i < edges.Length; i++) {
            int src = edges[i][0], dest = edges[i][1];
            double prob = succProb[i];
            adjList[src].Add((dest, prob));
            adjList[dest].Add((src, prob));
        }

        Dictionary<int, double> visited = new();
        PriorityQueue<int, double> maxHeap = new(Comparer<double>.Create((a,b) => b.CompareTo(a)));
        maxHeap.Enqueue(start_node, 1);
        while (maxHeap.TryDequeue(out int currNode, out double currProb)) {
            if (visited.ContainsKey(currNode)) continue;
            visited[currNode] = currProb;

            foreach (var (neighborNode, neighborProb) in adjList[currNode]) {
                if (!visited.ContainsKey(neighborNode)) {
                    maxHeap.Enqueue(neighborNode, neighborProb * currProb);
                }
            }
        }
        return visited.ContainsKey(end_node) ? visited[end_node] : 0;
    }
}