import random

def syllable(end_of_word=False):
  one_letter_onsets = "b c d f g h j k l m n p r s t v w y z".split()
  two_letter_onsets = '''sc sh sk sl sm sn sp st sw
                         pr br tr dr cr gr fr
                         pl bl kl cl gl fl
                         tw ph'''.split()
  three_letter_onsets = "spl spr str scr shr thr".split()

  0.175
  0.326

  onset = 's'
  nucleus = 'e'
  coda = 't'

  return onset + nucleus + coda

# Fix this to account for syllables shorter than 2 letters and with missing onsets or codas.
def make_many_syllables():
  rand = random.random()
  if   rand > 0.6752:  n = 1
  elif rand > 0.3909:  n = 2
  elif rand > 0.1954:  n = 3
  elif rand > 0.0533:  n = 4
  elif rand > 0.01777: n = 5
  else:                n = 6

  syllables = ''
  for _ in range(n-1):
    syllables += syllable()

  return syllables + syllable(end_of_word=True)

def make_word():
  two_letter_words = "if of ah oh ok am an in on up or as is us at it be by do go he hi me my no so to we".split()

  rand = random.random()
  if rand > 0.196:
    return make_many_syllables()
  elif rand > 0.028:
    return random.choice(two_letter_words)
  else:
    if random.random() > 0.025: return 'a'
    else:                       return 'I'

sentence = ''
for _ in range(100):
  sentence = sentence + ' ' + make_word()
print sentence