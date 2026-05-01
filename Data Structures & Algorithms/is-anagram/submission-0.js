class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let word1 = [...s]
        let sortedWord1 = word1.sort().toString()
        
        let word2 = [...t]
        let sortedWord2 = word2.sort().toString()

        console.log(sortedWord1)
        console.log(sortedWord2)
        return sortedWord1 == sortedWord2
    }
}
