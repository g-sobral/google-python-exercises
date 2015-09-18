from collections import Counter
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile

from wordcount.core import asc, top, lines, count, load


class SmartText(ScrolledText):
    @property
    def content(self):
        return self.text

    @content.setter
    def content(self, value):
        self.delete(1.0, tk.END)
        self.insert(tk.INSERT, value)


class CounterApplication(tk.Frame):
    COUNT = 1
    TOPCOUNT = 2

    MODES = {
        COUNT: asc,
        TOPCOUNT: top,
    }

    def __init__(self, master=None):
        super().__init__(master)
        self.mode = tk.IntVar()
        self.mode.set(self.COUNT)

        self.words = Counter()

        self.createWidgets()
        self.pack()

    def createWidgets(self):
        btn1 = tk.Button(self, text='Open File', command=self.on_load_words)
        btn1.pack(side=tk.TOP)

        rb1 = tk.Radiobutton(self, variable=self.mode, value=self.COUNT, command=self.on_show_words, text='Count')
        rb1.pack(side=tk.TOP)

        rb2 = tk.Radiobutton(self, variable=self.mode, value=self.TOPCOUNT, command=self.on_show_words, text='Top count')
        rb2.pack(side=tk.TOP)

        self.text_area = SmartText()
        self.text_area.pack(side=tk.BOTTOM)

    def on_load_words(self):
        with askopenfile() as f:
            self.words = count(load(f))
            self.on_show_words()

    def on_show_words(self):
        cmd = self.MODES[self.mode.get()]
        self.text_area.content = lines(cmd(self.words))


def gui():
    root = tk.Tk()
    app = CounterApplication(master=root)
    app.mainloop()