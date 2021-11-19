def countSyllables(word, debug=False):#a word is a string containing ONLY alphabetical characters
    if not word.isalpha():
        return 0
    vowels = 'a e i o u y'.split(' ')
    totalSyllables = 0
    word = word.lower()
    for i in range(len(word)):
        if(debug):
            print(word[i]+":")
        
        if(word[i] in vowels):
            if(debug):
                print("    is a vowel")
            
            if(i<len(word)-1):
                if(debug):
                    print("    not last letter")
                
                if(word[i+1] in vowels):
                    if(debug):
                        print("    next letter is vowel")
                else:
                    if(debug):
                        print("    next letter is not vowel")
                        print("    ADD SYL")
                    totalSyllables+=1
            else:
                if(debug):
                    print("    last letter")
                    print("    ADD SYL")
                totalSyllables+=1
            
            
    return(totalSyllables)
