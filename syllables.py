def syl(word):#a word is a string containing ONLY alphabetical characters
    vow = 'a e i o u y'.split(' ')
    syl = 0
    for i in range(len(word)):
        print(word[i]+":")
        
        if(word[i] in vow):
            print("    is a vowel")
            
            if(i<len(word)-1):
                print("    not last letter")
                
                if(word[i+1] in vow):
                    print("    next letter is vowel")
                else:
                    print("    next letter is not vowel")
                    print("    ADD SYL")
                    syl+=1
            else:
                print("    last letter")
                print("    ADD SYL")
                syl+=1
            
            
    return(syl)
