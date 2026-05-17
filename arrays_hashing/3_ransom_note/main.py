class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        freqRansomNote = {}
        freqMagazine = {}
        for char in magazine:
            freqMagazine[char] = freqMagazine.get(char,0) + 1
        for char in ransomNote:
            if char not in freqMagazine:
                return False
            freqRansomNote[char] = freqRansomNote.get(char,0) + 1
        
        for key in freqRansomNote:
            if freqRansomNote[key] > freqMagazine[key]:
                return False
        return True
