# Aiyush Gupta 10ST
# String Manipulation
# Task 22

import passage



passage = passage.text.lower()
passage = passage.replace(",", "")
passage = passage.replace("-", "")
passage = passage.replace(".", "")
passage = passage.split()

avr = sum(len(word) for word in passage) / len(passage)
print (avr)
