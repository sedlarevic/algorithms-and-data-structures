class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        startWindow = 0
        hashseqs = {}
        for endWindow in range(10,len(s)+1):
            substr = s[startWindow:endWindow]
            hashseqs[substr] = hashseqs.get(substr, 0) + 1
            startWindow += 1

        seqs = [key for key, value in hashseqs.items() if value > 1]
        return seqs
