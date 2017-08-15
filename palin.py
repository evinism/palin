import random
import sys
import itertools

# step 1:
# easy grammar
# "" is a palindrome
# word + palindrome + reversed_word is a palindrome

continue_chance = 0.7

# get words ordered by count
with open('count_1w.txt') as f:
  words_ordered_by_count = [line.split()[0] for line in list(f.read().splitlines())]

with open('/usr/share/dict/words') as f:
  word_set = set(f.read().splitlines())

reject_list = set(list("bcdefghjklmnopqrstuvwxyz"))

def is_valid_english_word(word):
  return word in word_set and word not in reject_list

dictionary = [word for word in words_ordered_by_count if is_valid_english_word(word)]

# building l reversibles
def brute_force_reversibles(level, num_of_entries = 1000000):
  dict_tuples = list(itertools.combinations(dictionary[:num_of_entries], level))
  # create a lookup for joined to unjoined
  joined_to_unjoined = {}
  for item in dict_tuples:
    joined_to_unjoined[''.join(item)] = ' '.join(item)
  # the lookup set to see whether a joined combo exists
  joined_set = set(joined_to_unjoined.keys())

  reversibles = [(joined_to_unjoined[joined], joined_to_unjoined[joined[::-1]]) for joined in joined_set if (joined[::-1] in joined_set)]
  return reversibles

l1_reversibles = brute_force_reversibles(1, 10000)
l2_reversibles = brute_force_reversibles(2, 3000)

reversible_sets = [
  l1_reversibles,
  l2_reversibles
]

def getReversible():
  reversible_set = random.choice(reversible_sets)
  choice = random.choice(reversible_set)
  return choice

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

def run_forever():
  while 1:
    print(generate())

run_forever()
