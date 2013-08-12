import random

def syllable(end_of_word=False):



  onset = 'a'
  nucleus = 'b'
  coda = 'c'

  return onset + nucleus + coda

def word():
  rand = random.randrange(70)
  if   rand in range(32):     n = 1
  elif rand in range(32, 48): n = 2
  elif rand in range(48, 59): n = 3
  elif rand in range(59, 67): n = 4
  elif rand in range(67, 69): n = 5
  elif rand in range(69, 70): n = 6
  else: raise ValueError("Random number out of range")

  syllables = ''
  for _ in range(n-1):
    syllables += syllable()

  return syllables + syllable(True)

for _ in range(30):
  print word()