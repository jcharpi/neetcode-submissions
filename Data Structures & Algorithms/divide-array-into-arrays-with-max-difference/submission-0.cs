public class Solution {
    public int[][] DivideArray(int[] nums, int k) {
        List<List<int>> result = [];
        int groupsNeeded = nums.Length / 3;
        Array.Sort(nums);

        for (int i = 0; i < groupsNeeded; i++) {
            result.Add(new List<int>());
        }

        int currArr = 0;
        foreach (int num in nums) {
            result[currArr].Add(num);
            if (result[currArr].Count == 3) { 
                if (result[currArr][2] - result[currArr][0] > k) return [];
                currArr++;
            }
        }

        foreach (List<int> entry in result) {
            Console.WriteLine(string.Join(", ", entry)); 
        }
        return result.Select(group => group.ToArray()).ToArray();
    }
}
