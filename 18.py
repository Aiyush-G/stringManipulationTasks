# Aiyush Gupta 10ST
# String Manipulation
# Task 18 - Reverse
import passage
# Access text as passage.text
listing = list(passage.text.split())
backwards = []

for i in listing:
    i = i[::-1]
    backwards.append(i)
    
print (*backwards)

