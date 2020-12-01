class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for w in words:
            mw = ""
            for c in w:
                mw += morse[ord(c)-97]
            s.add(mw)
        return len(s)