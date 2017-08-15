import sys
import random

for line in sys.stdin:
  splitLine = line.split()
  random.shuffle(splitLine)
  print(" ".join(splitLine))
