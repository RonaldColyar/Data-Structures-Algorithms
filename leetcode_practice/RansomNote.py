class Solution:
    def place_letters(self,table,string):
        #place the letters with how many times its seen
        for letter in string:
                if letter in table:
                    table[letter] +=1
                else:
                    table[letter] = 1

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            #table of how many times each letter is seen
            note = {}
            mag = {}
            self.place_letters(note,ransomNote)
            self.place_letters(mag, magazine)

            for letter in ransomNote:
                #if letter in both strings
                if letter in note and letter in mag:
                    #if the letter count of the magazine is less than the note
                    if   mag[letter] < note[letter]:
                        return False
                # if the letter is in the note and not in magazine
                elif letter in note and letter not in mag:
                    return False
            #everything checks out
            return True
                        
            
            
            
            