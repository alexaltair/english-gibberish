import random

def syllable(end_of_word=False):
  one_letter_onsets = "b c d f g h j k l m n p r s t v w y".split()
  two_letter_onsets = '''sc sh sk sl sm sn sp st sw
                         pr br tr dr cr gr fr
                         pl bl cl gl fl
                         tw ph'''.split()
  three_letter_onsets = "z spl spr str scr shr thr".split()

  vowels = "a e i o u".split()
  digraphs = "y ai au ea ee ei eo eu ia ie io iu oa oe oi oo ou ua ue ui uo".split()

  one_letter_codas = "b d f g h k m n p t w x".split()
  # Maybe l or r
  two_letter_codas = "mp nt nd nk nz ve ce ze wn ck pt ft st sk sp ch th".split()
  double_letter_codas = "bb dd ff gg ll mm nn pp rr ss tt".split()
  rare_codas = "tch dge nge pth nch nt".split()
  optional_word_endings = "y s es ed e".split()

  # 0.175 p that onset is empty
  # 0.326 prob that coda is empty

  onset = random.choice(100*one_letter_onsets + 10*two_letter_onsets + three_letter_onsets)
  nucleus = random.choice(10*vowels + digraphs)
  if end_of_word:
    coda = random.choice(3*[''] + one_letter_onsets)
  else:
    coda = ''

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
for _ in range(200):
  sentence = sentence + ' ' + make_word()
print sentence