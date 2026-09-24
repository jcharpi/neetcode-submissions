public class Solution {
    public int NetworkDelayTime(int[][] times, int n, int k) {
        Dictionary<int, List<(int dest, int cost)>> adjList = new();
        foreach (int[] time in times) {
            int src = time[0], dest = time[1], cost = time[2];
            if (!adjList.ContainsKey(src)) adjList[src] = new();
            adjList[src].Add((dest, cost));
        }

        Dictionary<int, int> shortest = new();
        PriorityQueue<int, int> minHeap = new();
        minHeap.Enqueue(k, 0);
        while (minHeap.TryDequeue(out int currNode, out int currCost)) {
            if (shortest.ContainsKey(currNode)) continue;
            shortest[currNode] = currCost;

            if (!adjList.TryGetValue(currNode, 
                out List<(int dest, int cost)> neighbors)) continue;
            
            foreach ((int neighborNode, int neighborCost) in neighbors) {
                if (!shortest.ContainsKey(neighborNode)) {
                    minHeap.Enqueue(neighborNode, neighborCost + currCost);
                }
            }
        }

        return shortest.Count != n ? -1 : shortest.Values.Max();
    }
}
