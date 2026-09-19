public class Solution {
    public List<int> PartitionLabels(string s) {
        Dictionary<char, int> lastIndexes = new Dictionary<char, int>();
        for (int i = 0; i < s.Length; i++) lastIndexes[s[i]] = i;

        List<int> output = new List<int>();
        int currSubstrCount = 0, partitionEnd = 0;
        for (int i = 0; i < s.Length; i++) {
            partitionEnd = Math.Max(partitionEnd, lastIndexes[s[i]]);
            currSubstrCount++;
            if (i == partitionEnd) {
                output.Add(currSubstrCount);
                currSubstrCount = 0;
            }
        }
        return output;
    }
}
