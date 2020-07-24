#!/usr/bin/python3
"""
Script that takes an argument 2 strings
First argument is the name of the Markdown file
Second argument is the output file name
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

