class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hash = new Map()
        let result = []
        for(let index in nums) {
            let p = target - nums[index]
            let c = nums[index]
            if(hash.has(c)) {
                result = [Number(index), Number(hash.get(c))]
            } else {
                hash.set(p, index)
            }
        }
        return result

    }
}