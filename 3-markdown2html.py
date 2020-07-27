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
    with open(destination, "w") as d:
        ul_amount = 0
        ol_amount = 0
        for line in lines:
            h_level = line.count("#")
            h_open = ("<h{}>".format(h_level))
            h_close = ("</h{}>".format(h_level))
            ul_open = ("<ul>")
            ul_close = ("</ul>")
            ol_open = ("<ol>")
            ol_close = ("</ol>")
            li_open = ("<li>")
            li_close = ("</li>")
            sp = line.find(" ")
            tag_content = line[sp+1: -1]
            hyphen = line.startswith("-")
            asterisk = line.startswith("*")
            if h_level > 0:
                tag_open = h_open
                tag_close = h_close
                html_line = ("{}{}{}\n".format(tag_open, tag_content, tag_close))
            if hyphen == True:
                ul_amount += 1
                tag_open = li_open
                tag_close = li_close
                if ul_amount == 1:
                    html_line = ("{}\n{}{}{}\n".format(ul_open, tag_open, tag_content, tag_close))
                if ul_amount > 1:
                    html_line = ("{}{}{}\n{}\n".format(tag_open, tag_content, tag_close, ul_close))
            if asterisk == True:
                ol_amount += 1
                tag_open = li_open
                tag_close = li_close
                if ol_amount == 1:
                    html_line = ("{}\n{}{}{}\n".format(ol_open, tag_open, tag_content, tag_close))
                if ol_amount > 1:
                    html_line = ("{}{}{}\n{}\n".format(tag_open, tag_content, tag_close, ol_close))
            d.write(html_line)
