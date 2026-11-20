public class Solution {
    public List<int> MajorityElement(int[] nums) {
        HashSet<int> result = [];
        Dictionary<int, int> numToCounts = [];
        int threshold = nums.Length / 3;

        foreach (int num in nums) {
            numToCounts.TryGetValue(num, out int count);
            int newCount = count + 1;
            numToCounts[num] = newCount;
            
            if (newCount > threshold) result.Add(num);
        }

        return result.ToList();
    }
}