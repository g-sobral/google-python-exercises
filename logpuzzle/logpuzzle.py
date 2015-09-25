#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

from pathlib import Path
import re
import argparse
from urllib.request import urlretrieve
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(logfile):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    match_server = re.search(r'(?<=_)\S+', str(logfile))
    server = 'https://' + match_server.group(0)

    log = logfile.open('r').read()

    paths = set(re.findall(r'(?<=GET )\S+', log))
    puzzle_paths = [p for p in paths if 'puzzle' in p]
    urls = [urljoin(server, p) for p in puzzle_paths]

    return sorted(urls, key= lambda x: x[x.rfind('-') + 1:])


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    htmlfile = dest_dir / 'index.html'
    html = '<verbatim>\n<html>\n<body>\n'

    images = {}
    for idx, url in enumerate(img_urls):
        filepath = dest_dir / ''.join(('img', str(idx), '.jpg'))
        html = ''.join((html, '<img src=\"', str(filepath), '\">'))
        images[url] = str(filepath)
    html += '</body>\n</html>'
    htmlfile.open('w').write(html)

    print('downloading images...')
    with ThreadPoolExecutor(max_workers=50) as executor:
        for url, filename in images.items():
            executor.submit(urlretrieve, url, filename)
    print('done!')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--todir', type=str, help='download images to directory')
    parser.add_argument('logfile', type=str, help='apache log file with hidden urls')
    options = parser.parse_args()

    img_urls = read_urls(Path(options.logfile))

    if options.todir:
        destdir = Path(options.todir).resolve()
        download_images(img_urls, destdir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
