public class Solution {
    public int CanCompleteCircuit(int[] gas, int[] cost) {
        int tank = 0, startIndex = 0;

        if (gas.Sum() < cost.Sum()) return -1;

        for (int i = 0; i < gas.Length; i++) {
            tank += gas[i] - cost[i];
            if (tank < 0) {
                startIndex = i + 1;
                tank = 0;
            }
        }

        return startIndex;
    }
}
