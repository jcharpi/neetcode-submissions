public class Solution {
    public int[][] DivideArray(int[] nums, int k) {
        int groupsNeeded = nums.Length / 3;
        int[][] result = new int[groupsNeeded][];
        Array.Sort(nums);

        for (int i = 0; i < groupsNeeded; i++) {
            result[i] = new int[3];
        }

        int currArr = 0, arrIndex = 0;
        foreach (int num in nums) {
            result[currArr][arrIndex] = num;
            arrIndex++;
            if (arrIndex == 3) { 
                if (result[currArr][2] - result[currArr][0] > k) return [];
                currArr++;
                arrIndex = 0;
            }
        }
        
        return result;
    }
}
