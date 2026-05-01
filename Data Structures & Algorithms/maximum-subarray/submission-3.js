class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let maxSub = nums[0]
        let currSub = 0

        for(let num of nums) {
            if(currSub < 0) {
                currSub = 0
            }
            currSub += num
            maxSub = Math.max(maxSub, currSub)
        }
        return maxSub
    }
}
