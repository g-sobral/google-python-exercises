from collections import Counter


def load(f):
    return f.read()

def count(content):
    return Counter(content.lower().split())

def asc(words):
    return sorted(words.items())

def top(words, qty=20):
    return words.most_common(qty)

def lines(words):
    lines_ = ('{}\t\t{}'.format(*t) for t in words)
    return '\n'.join(lines_)

def count_words(filename):
    return lines(asc(count(load(filename))))

def top_count(filename, qty):
    print('topcount')
    return lines(top(count(load(filename)), qty))