#!/usr/bin/python3
"""
Markdown is awesome! All your README.md are made in Markdown,
but do you know how Github are rendering them?
It’s time to code a Markdown to HTML!
"""
from sys import argv, stderr, exit
from os import path
if __name__ == "__main__":
    size = len(argv)
    if size < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    check = path.exists(argv[1])
    if (check is False):
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
    with open(argv[1], 'r') as md:
        mdlines = md.readlines()
        _lines = []
        for line in mdlines:
            _list = line.split()
            _fchar = _list[0]
            _ochars = ' '.join(_list[1:])
            if _fchar[0] == '#':
                _hlevel = len(_fchar)
                _lines.append('<h{0}>{1}</h{0}>\n'.format(_hlevel, _ochars))
    with open(argv[2], 'w') as html:
        html.writelines(_lines)
    exit(0)

