import random
import sys
import itertools

# step 1:
# easy grammar
# "" is a palindrome
# word + palindrome + reversed_word is a palindrome

continue_chance = 0.9

with open('count_1w.txt') as f:
  dictionary = [line.split()[0] for line in list(f.read().splitlines())]

# building l1 reversibles
def build_reversibles(level, num_of_entries = 1000000):
  dict_tuples = list(itertools.combinations(dictionary[:num_of_entries], level))
  joined_set = set(map(lambda combo: ''.join(combo), dict_tuples))
  reversibles = [joined for joined in joined_set if (joined[::-1] in joined_set)]
  return reversibles

l1_reversibles = build_reversibles(1, 10000)
l2_reversibles = build_reversibles(2, 1000)

#print(l2_reversibles)

reversible_sets = [
  l1_reversibles,
  l2_reversibles
]

def getReversible():
  reversible_set = random.choice(reversible_sets)
  choice = random.choice(reversible_set)
  return (choice, choice[::-1])

def wrap(palindrome):
  rev = getReversible()
  return rev[0] + " " + palindrome + " " + rev[1]

def generate():
  kernel = getReversible()
  palindrome = kernel[0] + " " + kernel[1]
  while continue_chance > random.random():
    palindrome = wrap(palindrome)
  return palindrome

def run(n):
  for i in range(n):
    print(generate())

run(10)
