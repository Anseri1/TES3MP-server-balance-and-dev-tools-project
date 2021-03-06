from tkinter import *
from tkinter import ttk
from stats_tools_module import distribution_tool
from stats_tools_module import fatigueTerm
from stats_tools_module import hit_chance


def main():
    root = Tk()
    root.title("tools menu")

    frame = ttk.Frame(root)
    frame.pack(padx=50)

    button1 = Button(frame, text="binomial distribution", command=distribution_tool.calculations)
    button1.pack()

    button2 = Button(frame, padx=16, text="fatigueTerm tool", command=fatigueTerm.fatigueStat)
    button2.pack()

    button3 = Button(frame, padx=38, text="hit chance", command=hit_chance.hitChanceStat)
    button3.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
