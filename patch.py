#!/usr/bin/env python

import fontforge
import sys
import os

target = sys.argv[1]
target_base = os.path.basename(target)
bold_target = sys.argv[2]
bold_target_base = os.path.basename(bold_target)

olddir = sys.argv[3] + "/"
f = fontforge.open(target)
# boldf = fontforge.open(bold_target)
oldf = fontforge.open(olddir + target_base)
oldboldf = fontforge.open(olddir + bold_target_base)

fnv = f.fontname.split("-");
if (len(fnv) != 2):
    raise Exception("Unexpeced fontname")
style = fnv[1]

# alternate symbols
CV = [
        ['zero', 'zero.zero'],

        ['five', 'five.cv20'],
        # ['five.dnom', 'five.dnom.cv20'],
        # ['five.numr', 'five.numr.cv20'],

        # ['f', 'f.cv09.ss20'],

        ['g', 'g.cv03'],
        ['uni01F5', 'uni01F5.cv03'],
        ['gbreve', 'gbreve.cv03'],
        ['gcaron', 'gcaron.cv03'],
        ['gcircumflex', 'gcircumflex.cv03'],
        ['uni0123', 'uni0123.cv03'],
        ['gdotaccent', 'gdotaccent.cv03'],

        # u and friends
        ['u', 'u.cv12'],
        ['uacute', 'uacute.cv12'],
        ['ubreve', 'ubreve.cv12'],
        ['ucircumflex', 'ucircumflex.cv12'],
        ['udieresis', 'udieresis.cv12'],
        ['uni1EE5', 'uni1EE5.cv12'],
        ['ugrave', 'ugrave.cv12'],
        ['uni1EE7', 'uni1EE7.cv12'],
        ['uhorn', 'uhorn.cv12'],
        ['uni1EE9', 'uni1EE9.cv12'],
        ['uni1EF1', 'uni1EF1.cv12'],
        ['uni1EEB', 'uni1EEB.cv12'],
        ['uni1EED', 'uni1EED.cv12'],
        ['uni1EEF', 'uni1EEF.cv12'],
        ['uhungarumlaut', 'uhungarumlaut.cv12'],
        ['umacron', 'umacron.cv12'],
        ['uogonek', 'uogonek.cv12'],
        ['uring', 'uring.cv12'],
        ['utilde', 'utilde.cv12'],
]

for [find, replace] in CV:
    f.removeGlyph(find)
    f.selection.select(replace)
    f.copy()
    f.selection.select(find)
    f.paste()

# old J
f.removeGlyph('J')
oldf.selection.select('J')
oldf.copy()
f.selection.select('J')
f.paste()

# Bold stuff
BV = [
        "exclam", "quotedbl", "numbersign",
        "dollar", "percent", "ampersand",
        "quotesingle", "parenleft", "parenright",
        "asterisk", "plus", "comma", "hyphen",
        "period", "slash", "colon", "semicolon",
        "less", "equal", "greater", "question",
        "at", "bracketleft", "backslash",
        "bracketright", "asciicircum",
        "underscore", "grave", "braceleft",
        "bar", "braceright", "asciitilde",
]

for g in BV:
    f.removeGlyph(g)
    oldboldf.selection.select(g);
    oldboldf.copy()
    f.selection.select(g);
    f.paste()

# fixup: https://github.com/JetBrains/JetBrainsMono/issues/334
# following values were taken from v2.001
f.os2_winascent = 1085
f.os2_windescent = 270
f.os2_typoascent = 970
f.os2_typodescent = -270
f.hhea_ascent = 970
f.hhea_descent = -270

# change font names and shit
fn = "NRK Mono"
f.fontname = fn.replace(" ", "") + "-" + style
f.familyname = fn
f.fullname = fn + " " + style
ver = f.version.split(";")[0]
uniq_id = ver + ";NM;" + fn.replace(" ", "") + "-" + style
f.appendSFNTName('English (US)', 'UniqueID', uniq_id);
# f.appendSFNTName('English (US)', 'Preffered Family', "NRK Mono");

outdir = "./"
if len(sys.argv) > 4:
    outdir = sys.argv[4] + "/"
o = outdir + fn + " " + style + ".ttf"
f.generate(o.replace(" ", "-"))
