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

  print("sub {0} @letters @letters @letters @letters {0}' by {1};".format(k, s[0]))
  print("sub {0} @letters @letters @letters {0}' by {1};".format(k, s[0]))
  print("sub {0} @letters @letters {0}' by {1};".format(k, s[0]))
  print("sub {0} @letters {0}' by {1};".format(k, s[0]))
  print("sub {0} {0}' by {1};".format(k, s[0]))

  if len(l) >= 2:
      print("sub {0} {0}.alt {0}' by {1};".format(k, s[1]))

print("feature salt { lookup salt1 {")
for k, l in D.items():
    if k+".alt" in l:
      print("sub {0} by {1};".format(k, k+".alt"))
print("} salt1; } salt;")

for fea in ["ss02", "ss03", "ss04", "ss05"]:
    print("feature {0} {{ lookup {0}1 {{".format(fea))
    for k, l in D.items():
        if k+'.'+fea in l:
          print("sub {0} by {1};".format(k, k+'.'+fea))
    print("}} {0}1; }} {0};".format(fea))

