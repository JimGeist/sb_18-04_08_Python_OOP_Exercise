# sb_18-04_08_Python_OOP_Exercise

## Python OO Practice 

Creation of SerialGenerator, WordFinder, and SpecialWordFinder classes. 


## Assignment Details
**ASSIGNMENT INVOLVED**:
- SerialGenerator class with .generate() method to return the next serial number and .reset() to reset the serial number genderator back to the starting value.
- WordFinder class . . which, oddly, does not find a word but instead returns a random word. WordFinder expects a filename with path to a text file with one word per line. The contents of the text file is stored as a word list within the class. The .random() method returns one random from the word list.
- SpecialWordFinder class is an extension of the WordFinder class. SpecialWordFinder ignores words that begin with a # and blank lines.

All classes include doctests and data validations.


**DATA FILES**:
./data/cats - File has 4 cat names. Used to initially test reading from a file.
./data/cats2 - 6 cat names, some with leading and trailing spaces. Used to test strip of leading and trailing spaces. 
./data/doctest_swf.txt - 7 words (some with leading/trailing spaces), 2 words that begin with a #, 2 blank lines. File is used on the SpecialFindWord doctests.
./data/doctest_wf.txt - 5 words. File is used on the FindWord doctexts
./data/SpecialWordFind.txt - the example in the assignment handout (# Veggies, # Fruit, 4 words, 3 blank lines)
./data/words.txt - the dictionary with 235,886 words.


**TIMING**:
- 213 minutes -- 33 minutes over the high side. Some of the additional time resulted from adding blank line and ignored word counters to the SpecialWordFinder class and existing variables were renamed. For serial.py, the initial attempt had try, assert / except blocks but they were changed to raise errors instead when start serial number is not a number or not greater than 0.


