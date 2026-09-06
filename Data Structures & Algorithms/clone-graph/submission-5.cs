/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

public class Solution {
    public Node CloneGraph(Node node) {
		if (node == null) return null;
		Dictionary<Node, Node> originalToClone = new Dictionary<Node, Node>();
		Node dfs(Node original) {
			if (originalToClone.ContainsKey(original)) return originalToClone[original];

			Node clone = new Node(original.val);
			originalToClone[original] = clone;
			
			foreach (Node neighbor in original.neighbors) clone.neighbors.Add(dfs(neighbor));
			return clone;
		}
		return dfs(node);
    }
}
