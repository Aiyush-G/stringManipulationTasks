# Aiyush Gupta 10ST
# String Manipulation
# Task 4 - number of vowels in paragraph

import passage
# Access text as passage.text

# Map:
'''Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed,
function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator
stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().'''

# * Removes Formatting


print (sum(list(map(passage.text.lower().count, "aeiou"))))

