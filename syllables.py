def syl(word, debug=False):#a word is a string containing ONLY alphabetical characters
    vow = 'a e i o u y'.split(' ')
    syl = 0
    for i in range(len(word)):
        if(debug):
            print(word[i]+":")
        
        if(word[i] in vow):
            if(debug):
                print("    is a vowel")
            
            if(i<len(word)-1):
                if(debug):
                    print("    not last letter")
                
                if(word[i+1] in vow):
                    if(debug):
                        print("    next letter is vowel")
                else:
                    if(debug):
                        print("    next letter is not vowel")
                        print("    ADD SYL")
                    syl+=1
            else:
                if(debug):
                    print("    last letter")
                    print("    ADD SYL")
                syl+=1
            
            
    return(syl)
