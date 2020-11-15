# Aiyush Gupta 10ST
# String Manipulation
# Task 25 - Ceaser Cypher

import passage
shift = -9
# zip() joins two tuples together
lower = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
upper = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))

encoded = ''
for x in passage.text.upper():
    if x.isalpha():
        encoded = lower[ (upper[x] + shift)%26 ] + encoded
    else:
        encoded = x + encoded

print (encoded)

