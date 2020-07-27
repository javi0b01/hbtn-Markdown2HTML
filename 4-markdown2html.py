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
        for line in range(0, len(lines) - 1):
            current = lines[line]
            the_next = lines[line + 1]
            h_level = current.count("#")
            h_open = ("<h{}>".format(h_level))
            h_close = ("</h{}>".format(h_level))
            ul_open = ("<ul>")
            ul_close = ("</ul>")
            ol_open = ("<ol>")
            ol_close = ("</ol>")
            li_open = ("<li>")
            li_close = ("</li>")
            p_open = ("<p>")
            p_close = ("</p>")
            line_break = ("<br/>")
            space = current.find(" ")
            ishash = current.startswith("#")
            ishyphen = current.startswith("-")
            isasterisk = current.startswith("*")
            isnew_line = current.startswith("\n")
            if ishash is True or ishyphen is True or isasterisk is True or isnew_line is True:
                isparagraph = False
                tag_content = current[space+1: -1]
            else:
                isparagraph = True
                tag_content = current[0: -1]
                current_line = tag_content.islower()
                next_content = the_next[0: -1]
                next_line = next_content.islower()
            if ishash == True:
                if h_level > 0:
                    tag_open = h_open
                    tag_close = h_close
                    html_line = ("{}{}{}\n".format(tag_open, tag_content, tag_close))
            if ishyphen == True:
                ul_amount += 1
                tag_open = li_open
                tag_close = li_close
                if ul_amount == 1:
                    html_line = ("{}\n{}{}{}\n".format(ul_open, tag_open, tag_content, tag_close))
                if ul_amount > 1:
                    html_line = ("{}{}{}\n{}\n".format(tag_open, tag_content, tag_close, ul_close))
            if isasterisk == True:
                ol_amount += 1
                tag_open = li_open
                tag_close = li_close
                if ol_amount == 1:
                    html_line = ("{}\n{}{}{}\n".format(ol_open, tag_open, tag_content, tag_close))
                if ol_amount > 1:
                    html_line = ("{}{}{}\n{}\n".format(tag_open, tag_content, tag_close, ol_close))
            if isnew_line == True:
                html_line = ("")
            if isparagraph == True:
                tag_open = p_open
                if next_line == True:
                    tag_close = line_break
                    html_line = ("{}\n{}\n{}\n".format(tag_open, tag_content, tag_close))
                if next_line == False:
                    tag_close = p_close
                    html_line = ("{}\n{}\n{}\n".format(tag_open, tag_content, tag_close))
                if current_line == True:
                    html_line = ("{}\n{}\n".format(tag_content, tag_close))
            d.write(html_line)
