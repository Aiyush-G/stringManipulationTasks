# Aiyush Gupta 10ST
# String Manipulation
# Task 5 - mostCommon

import passage
# Access text as passage.text
alphabet = 'abcdefghijklmnopqrstuvwxyz'
b = (sorted((list(zip(alphabet,list(map(passage.text.lower().count, alphabet))))),key=lambda l:l[1], reverse = True))[:10]
print (b)
