# Aiyush Gupta 10ST
# String Manipulation
# Task 8 - State range of characters to print out

import passage
# Access text as passage.text
# Note that this is character not index, that is why we -1
l1 = int(input("Enter position of the first character ")) -1
l2 = int(input("Enter position of the second character ")) -1
x = list(passage.text)[l1:l2]
print (x)
