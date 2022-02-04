#!/usr/bin/env python3
# file = open("/home/slytren/nameinput/nameprog2.txt", "r")
# count = 0
# for line in file:
#     words = line.split(" ")
#     count += len(words)

# file.close()
# print("Number of words in a text file : ", count)
from collections import defaultdict
d = defaultdict (int)
for letter in open("/home/slytren/nameinput/nameprog2.txt").read():
    d[letter] += 1
print(d, end=" ")