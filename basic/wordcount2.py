#!/usr/bin/python -tt
import argparse
from collections import Counter
import tkinter as tk
from tkinter import filedialog

def load(filename):
    with open(filename, 'r') as f:
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
    parser.add_argument('textfile')

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

            self.file_opt = {}
            self.file_opt['defaultextension'] = '.txt'
            self.file_opt['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
            self.file_opt['initialdir'] = '.'
            self.file_opt['initialfile'] = 'alice.txt'
            self.file_opt['parent'] = root

            self.select_file = tk.Button(self, text='Select text file', command=self.getFilename).pack(side='top')

            self.count = tk.Button(self, text='Count', command=self.c_words).pack(side='top')
            self.tcount = tk.Button(self, text='Top Count', command=self.t_words).pack(side='top')

            self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy).pack(side="bottom")

        def c_words(self):
            print(count_words(self.filename))

        def t_words(self):
            print(top_count(self.filename))

        def getFilename(self):
            self.filename = filedialog.askopenfilename(**self.file_opt)
            print(self.filename)

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    gui()
