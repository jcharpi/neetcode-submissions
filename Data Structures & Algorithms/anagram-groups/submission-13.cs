public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> hm = new Dictionary<string, List<string>>();
        foreach (string word in strs) {
            int[] counts = new int[26];
            foreach (char c in word) {
                counts[c - 'a']++;
            }

            string key = string.Join('#', counts);
            if (!hm.ContainsKey(key)) {
                hm[key] = new List<string>();
            }
            hm[key].Add(word);
        }
        return new List<List<string>>(hm.Values);
    }
}
