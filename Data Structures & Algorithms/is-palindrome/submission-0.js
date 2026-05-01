class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let sArray = [...s.trim()]
        let alphaNumArray = []
        for(let char of sArray) {
            if(isAlphanumeric(char)) {
                alphaNumArray.push(char)
            }
        }
        let originalString = alphaNumArray.join('').toLowerCase()
        let reversedString = alphaNumArray.reverse().join('').toLowerCase()
        return originalString === reversedString
    } 
}

function isAlphanumeric(char) {
    return /^[a-zA-Z0-9]$/.test(char);
}  
