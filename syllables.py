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
                if word[i] == "e":
                    # Bossy E
                    if(debug):
                        print("    last letter is E")
                else:
                    if(debug):
                        print("    last letter is not E")
                        print("    ADD SYL")
                    totalSyllables+=1
            
    if totalSyllables == 0: #if you found nothing, even though there was real text, you found at least something
        totalSyllables = 1
    return(totalSyllables)
