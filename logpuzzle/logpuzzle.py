#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    match_server = re.search(r'(?<=_)\S+', filename)
    server = match_server.group(0)

    with open(filename, 'r') as f:
        log = f.read()
        f.close()

    paths = re.findall(r'(?<=GET )\S+', log)
    puzzle_paths = [p for p in paths if 'puzzle' in p]

    urls = []
    for p in puzzle_paths:
        url = ''.join(('http://', server, p))
        if not url in urls:
            urls.append(url)

    return sorted(urls, key= lambda x: x[x.rfind('-') + 1:])



def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    dest_dir = os.path.abspath(dest_dir)

    html = '<verbatim>\n<html>\n<body>\n'

    img_idx = 0
    for url in img_urls:
        print(url)
        filename = ''.join((dest_dir, '/img', str(img_idx), '.jpg'))
        html = ''.join((html, '<img src=\"', filename, '\">'))
        urllib.urlretrieve(url, filename=filename)
        img_idx += 1

    html += '</body>\n</html>'

    with open(''.join((dest_dir, '/index.html')), 'w') as htmlfile:
        htmlfile.write(html)
        htmlfile.close()


def main():
    args = sys.argv[1:]

    if not args:
        print()
        'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print
        '\n'.join(img_urls)


if __name__ == '__main__':
    main()
