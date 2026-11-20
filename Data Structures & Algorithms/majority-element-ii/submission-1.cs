public class Solution {
    public List<int> MajorityElement(int[] nums) {
        int candidateA = -1, candidateB = -1;
        int countA = 0, countB = 0;

        foreach (int num in nums) {
            if (num == candidateA) countA++;
            else if (num == candidateB) countB++;
            else if (countA == 0) {
                candidateA = num;
                countA = 1;
            }
            else if (countB == 0) {
                candidateB = num;
                countB = 1;
            }
            else {
                countA--;
                countB--;
            }
        }

        countA = countB = 0;
        foreach (int num in nums) {
            if (num == candidateA) countA++;
            else if (num == candidateB) countB++;
        }

        List<int> result = [];
        if (countA > nums.Length / 3) result.Add(candidateA);
        if (countB > nums.Length / 3) result.Add(candidateB);

        return result;
    }
}