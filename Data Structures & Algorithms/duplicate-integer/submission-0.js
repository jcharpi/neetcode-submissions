class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let numDups = new Map();
        for(let num of nums) {
            if(numDups.has(num)) {
                return true
            } else {
                numDups.set(num, true)
            }
        }
        return false

    }
    
    
}
