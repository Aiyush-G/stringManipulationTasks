# Aiyush Gupta 10ST
# String Manipulation
# Task 15 - Upper Case all Vowels
import passage
# Access text as passage.text
for vowel in 'aeiou':
    x = passage.text.lower().replace(vowel, vowel.upper())

print (x)
