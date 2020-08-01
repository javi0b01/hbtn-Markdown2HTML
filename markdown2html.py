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
    with open(origin, "r") as o:
        lines = o.readlines()
    with open(destination, "x") as d:
        for line in lines:
            amount = line.count("#")
            tag_open = ("<h{}>".format(amount))
            tag_close = ("</h{}>".format(amount))
            sp = line.find(" ")
            tag_content = line[sp+1: -1]
            html_line = ("{}{}{}\n".format(tag_open, tag_content, tag_close))
            d.write(html_line)
    exit(0)

