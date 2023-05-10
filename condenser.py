#!/usr/bin/env python

import fontforge
import psMat
import sys

font = fontforge.open(sys.argv[1]);
for g in font.glyphs():
    g.transform(psMat.scale(0.94, 1.0))

fnv = font.fontname.split("-");
if (len(fnv) != 2):
    raise Exception("Unexpeced fontname")
style = fnv[1]
o = font.familyname + " Condensed " + style + ".ttf"
o = o.replace(" ", "-")

font.fontname = fnv[0] + "Condensed-" + style
font.familyname=font.familyname + " Condensed"
font.fullname=font.fullname + " Condensed"

d = "./"
if len(sys.argv) > 2:
    d = sys.argv[2] + "/"
font.generate(d + o)
