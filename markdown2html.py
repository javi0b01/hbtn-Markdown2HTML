#!/usr/bin/python3
"""
Markdown is awesome! All your README.md are made in Markdown,
but do you know how Github are rendering them?
It’s time to code a Markdown to HTML!
"""
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

