# This generates the contextual alternates

import fontforge
import string

print("@letters = [{}];".format(" ".join(list(string.ascii_letters))))

font = fontforge.fonts()[0]

D = dict()

for g in font.glyphs():
  if not '.' in g.glyphname:
    D[g.glyphname] = list()

for g in font.glyphs():
  if '.' in g.glyphname and g.glyphname.rpartition('.')[0] in D:
    D[g.glyphname.rpartition('.')[0]].append(g.glyphname)

for k, l in D.items():
  if len(l) == 0: continue

  if k not in list(string.ascii_letters): continue

  s = sorted(l)

  print("sub {0} @letters @letters {0}' by {1};".format(k, s[0]))
  print("sub {0} @letters {0}' by {1};".format(k, s[0]))
  print("sub {0} {0}' by {1};".format(k, s[0]))
