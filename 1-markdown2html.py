#!/usr/bin/python3
import sys
import os.path
if __name__ == "__main__":
    size = len(sys.argv)
    if size < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    check = os.path.isfile('./README.md')
    if (check is False):
        print("Missing <filename>")
        exit(1)
    origin = sys.argv[1]
    destination = sys.argv[2]
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
