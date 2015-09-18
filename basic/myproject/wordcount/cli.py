import argparse

from wordcount.core import count_words, top_count

def cli():
    parser = argparse.ArgumentParser(description='Conta palavras.')
    parser.add_argument('-c', '--count', action='store_true')
    parser.add_argument('-t', '--topcount', type=int)
    parser.add_argument('textfile', type=argparse.FileType())
    options = parser.parse_args()

    if options.count:
        print(count_words(options.textfile))
    elif options.topcount:
        print(top_count(options.textfile, options.topcount))