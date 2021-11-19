# Syllable Counter and Haiku Checker

## syllables.py
Given an input of an English word as a string, output the number of syllables it has.

```python
>>> import syllables
>>> syllables.countSyllables("syllables")
3
``` 
## haiku.py
Can check if a sentence follows a certain syllabic strucure, and more specifically can check if it follows that of a haiku

```python
>>> import haiku
>>> haiku.checkHaiku("This is a haiku, do you like what i have made? It is pretty pog")
[True, ['This is a haiku, ', 'do you like what i have made? ', 'It is pretty pog']]
>>> haiku.checkSyllabicStructure("it is the day to go and smell nature", [2, 2, 2, 2, 2])
[True, ['it is ', 'the day ', 'to go ', 'and smell ', 'nature']]
```
### Please feel free to make a pull request!
