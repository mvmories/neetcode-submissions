class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        for word_row in range(len(words)):
            for char_col in range(len(words[word_row])):
                if char_col >= len(words) or \
                   word_row >= len(words[char_col]) or \
                   words[word_row][char_col] != words[char_col][word_row]:
                    return False
        
        return True
        