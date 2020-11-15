# Aiyush Gupta 10ST
# String Manipulation
# Task 24 - Most Common Words

import passage
from collections import Counter
words = passage.text.split()
common = Counter(passage.text.split()).most_common(5)
print(common)
