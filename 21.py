# Aiyush Gupta 10ST
# String Manipulation
# Task 21

# How to solve
# Split into words
# Split words into letters (2D Array)
# Add a layer to the 2D array and assign each a value
# Add values
# Print


import passage
w= {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, " ":0}

passage = passage.text.lower()
passage = passage.replace(",", "")
passage = passage.replace("-", "")
passage = passage.replace(".", "")
passage = list(passage.split())

encoded = []

for z in passage:
    y = len(z)
    x = 0 
    for i in range(y):
        x = x +w[z[i]]
        encoded.append(x)

print (encoded)
        


