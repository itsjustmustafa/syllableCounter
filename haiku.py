import re
from syllables import countSyllables

def removePunct(sentence):
    puncts = ["'"]
    
    for punct in puncts:
        sentence = sentence.replace(punct, "")
    return sentence


# Checks whether a sentence (String) follows a syllabic structure (int list), eg. structure = [5, 7, 5] for a haiku
# a sentence follows a syllabic strucuture if it can be partitioned by words such that the nth partition has a total syllable count of the nth strucure value
def checkSyllabicStructure(sentence, structure, debug=False):
    words = re.split("\\b", removePunct(sentence))
    
    currentSyllabicStructure = [0 for i in structure]
    syllabicWordIndex = [[] for i in structure]
    syllabicIndex = 0
    
    badOutput = [False, []]
    for wordIndex in range(len(words)):
        word = words[wordIndex]
        
        if(debug):
            print("current word: {}".format(word))
        
        if syllabicIndex >= len(structure):
            if(debug):
                print("index too large")
            return badOutput
        
        currSyllables = countSyllables(word)
        
        # if current word fits into this structure, add the wordIndex to the list of indices and update syllable total
        if  currSyllables + currentSyllabicStructure[syllabicIndex] <= structure[syllabicIndex]:
            syllabicWordIndex[syllabicIndex].append(wordIndex)
            currentSyllabicStructure[syllabicIndex] += currSyllables
            if(debug):
                print("able to be fit")
                print("new syllabicWordIndex: {}".format(syllabicWordIndex))
                print("new currentSyllabicStructure: {}".format(currentSyllabicStructure))
        else: # current word too big for current group
            #check if this is the final group
            if syllabicIndex >= len(structure)-1:
                if(debug):
                    print("no next group to place word in")
                return badOutput
            elif currentSyllabicStructure[syllabicIndex] < structure[syllabicIndex]: #check if current group is not fulfilled
                if(debug):
                    print("last group not fullfilled")
                return badOutput
            elif currSyllables > structure[syllabicIndex + 1]:# check if current word is too big for next group
                if(debug):
                    print("current word too big for next group")
                return badOutput
            else: # Everything seems fine
                if(debug):
                    print("word added to next index")
                syllabicIndex += 1
                #print("new syllabicIndex: {}".format(syllabicIndex))
                syllabicWordIndex[syllabicIndex].append(wordIndex)
                currentSyllabicStructure[syllabicIndex] += currSyllables
    
    if(debug):
        print(syllabicWordIndex)
    if currentSyllabicStructure != structure:
        return badOutput
    else:
        wordPartitions = []
        for i in range(len(syllabicWordIndex)):
            wordPartitions.append("".join([words[j] for j in syllabicWordIndex[i]]))
        return [True, wordPartitions]
                

# checks whether a sentence follows a haiku structure, if so returns the sentence partitioned with the structure
def checkHaiku(sentence):
    return checkSyllabicStructure(sentence, [5,7,5])
    