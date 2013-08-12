This code considers only orthographics, not phonetics, for the simple reason that it is printing out letters and not sounds.
More or less ignores a variety of Greek influences.

Alphabet;
  b
  c
  d
  f
  g
  h
  j
  k
  l
  m
  n
  p
  q
  r
  s
  t
  v
  w
  x
  y
  z
  aeiou

Words smaller than three letters
  The only one letter words
    a I
  The only two letter words
    if of ah eh oh uh ok am um an in on up er or as is us at it aw ew ow ax ox be bi by do go ha he hi me my no so to we

Words three letters or larger

  Allowed onsets
    Empty string
    One letter
      b c d f g h j k l m n p r s t v w y z
      exceptions; qu
    Two letters
      sc sh sk sl sm sn sp squ st sw
      pr br tr dr cr gr fr
      pl bl kl cl gl fl
      tw ph
    Three letters
      spl spr str scr shr thr

  Allowed nuclei
    One letter
      a e i o u y
    Two letters
      .     ai    au
      ea ee ei eo eu
      ia ie    io iu
      oa oe oi oo ou
      ua ue ui uo

  Allowed codas
    Empty string
    One letter
      b d f g h k l m n p r t w x
    Two letters
      maybe   l r
      then    mp nt nd nk nz ve ce ze wn ck pt ft st sk sp ch th
              bb dd ff gg ll mm nn pp rr ss tt
      if eow,
      maybe   y s es ed e

    Three letters
      tch dge nge pth nch nt