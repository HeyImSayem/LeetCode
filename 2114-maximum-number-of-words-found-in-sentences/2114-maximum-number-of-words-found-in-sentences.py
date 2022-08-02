class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=0
        m=0
        for i in range(len(sentences)):
            c=sentences[i].count(' ')
            if c+1>m:
                m=c+1
        return m