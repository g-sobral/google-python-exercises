#!/usr/bin/python -tt
import argparse
from collections import Counter
import tkinter as tk

def load(f):
    return f.read()

def count(content):
    return Counter(content.lower().split())

def asc(words):
    return sorted(words.items())

def top(words, qty=20):
    return words.most_common(qty)

def lines(words):
    lines_ = ('{} {}'.format(*t) for t in words)
    return '\n'.join(lines_)

def count_words(filename):
    return lines(asc(count(load(filename))))

def top_count(filename):
    return lines(top(count(load(filename))))

###

def cli():
    parser = argparse.ArgumentParser(description='Conta palavras.')

    parser.add_argument('-c', '--count', action='store_true')
    parser.add_argument('-t', '--topcount', type=int)
    parser.add_argument('textfile', type=argparse.FileType())

    options = parser.parse_args()

    if options.count:
        print(count_words(options.textfile))
    elif options.topcount:
        print(top_count(options.textfile))


def gui():
    class Application(tk.Frame):
        def __init__(self, master=None):
            tk.Frame.__init__(self, master)
            self.pack()
            self.createWidgets()

        def createWidgets(self):
            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "Hello World\n(click me)"
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="top")

            self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                                command=root.destroy)
            self.QUIT.pack(side="bottom")

        def say_hi(self):
            print("hi there, everyone!")

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    gui()
