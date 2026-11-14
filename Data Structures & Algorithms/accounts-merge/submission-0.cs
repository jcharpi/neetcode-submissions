public class Solution {
    public List<List<string>> AccountsMerge(List<List<string>> accounts) {
        Dictionary<string, List<string>> adjList = [];

        foreach (List<string> account in accounts) {
            string src = account[1];
            adjList.TryAdd(src, []);

            for (int i = 2; i < account.Count; i++) {
                string dest = account[i];
                adjList.TryAdd(dest, []);

                adjList[src].Add(dest);
                adjList[dest].Add(src);
            }
        }

        List<List<string>> result = [];
        List<string> mergedAccount = [];
        HashSet<string> visited = [];

        void Dfs(string email) {
            if (visited.Contains(email)) return;

            visited.Add(email);
            mergedAccount.Add(email);
            foreach (string connectedEmail in adjList[email]) Dfs(connectedEmail);
        }

        foreach (List<string> account in accounts) {
            if (visited.Contains(account[1])) continue;
            string name = account[0];
            mergedAccount = [];
            Dfs(account[1]);
            mergedAccount.Sort();
            result.Add([name, ..mergedAccount]);
        }

        return result;
    }
}