class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let word1 = [...s]
        word1.sort()
        
        let word2 = [...t]
        word2.sort()

        return word1.toString() == word2.toString()
    }
}
