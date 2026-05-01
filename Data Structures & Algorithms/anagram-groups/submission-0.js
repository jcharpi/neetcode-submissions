class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let hash = new Map()

        for(let string of strs) {
            let sortedString = [...string].sort().join('')
            if(hash.has(sortedString)) {
                let currentValues = hash.get(sortedString)
                hash.set(sortedString, [...currentValues, string])
            } else {
                hash.set(sortedString, [string])
            }
        }
        return Array.from(hash.values())
    }
}
