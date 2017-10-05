def syl(word):#a word is a string containing ONLY alphabetical characters
    vow = 'a e i o u y'.split(' ')
    syl = 0
    for i in range(len(word)):
        if(word[i] in vow):
            syl+=1
            
    return(syl)
