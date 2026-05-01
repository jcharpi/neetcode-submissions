class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let symbolDict = new Map([
            ['(', ')'],
            ['[', ']'],
            ['{', '}'],
        ])

        let stack = []

        if(s.length % 2 == 1) {
            return false
        }

        for(let char of s) {
            if(char === '(' ||
            char === '{' ||
            char === '[') {
                stack.push(char)
            }
            else if(char !== symbolDict.get(stack.pop())) {
                return false
            }
        }
        return stack.length == 0


    
        
    }
}
