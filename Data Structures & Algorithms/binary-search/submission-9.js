class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let lowIndex = 0
        let highIndex = nums.length
        let numsCopy = nums.slice(lowIndex, highIndex)

        while(numsCopy.length > 2) {
            let mid = Math.floor(numsCopy.length/2)
            target > numsCopy[mid] ? lowIndex = mid : highIndex = mid
            if(target == numsCopy[mid]) { return nums.indexOf(numsCopy[mid]) }

            numsCopy = numsCopy.slice(lowIndex, highIndex+1)
            console.log(numsCopy)
        }

        let matchedVal = target == numsCopy[0] ? 0 : target == numsCopy[1] ? 1 : -1
        
        if(matchedVal != -1) {
            console.log(matchedVal)
            return nums.indexOf(numsCopy[matchedVal])
        } else {
            return matchedVal
        }
    }
}
