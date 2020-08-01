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
    origin = argv[1]
    destination = argv[2]
    with open(origin, 'r') as o:
        lines = o.readlines()
        html_lines = []
        for line in lines:
            _list = line.split()
            _fchar = _list[0]
            _ochars = ' '.join(_list[1:])
            if _fchar[0] == '#':
                _hlevel = len(_fchar)
                html_lines.append('<h{0}>{1}</h{0}>\n'.format(_hlevel, _ochars))
    with open(destination, 'w') as d:
        d.writelines(html_lines)
    exit(0)

