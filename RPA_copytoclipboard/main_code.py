import tkinter as tk
import copy_to_clipboard as ctc
import os

BASEPATH = os.path.dirname(os.path.realpath(__file__))

class app(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Copy Image to Clipboard")

        # UI
        self.root.geometry("600x700+1000+100")
        self.root.resizable(False, False)
        self.label = tk.Label(self.root,
                            font="100",
                            bg="gray",
                            fg="white",
                            text="How To Use\n\n1. Locate your image file in this exe file folder\n\n2. Put image file name\n\n3. use ctrl + v")
        self.ent = tk.Entry(self.root, font="100")
        self.ent.focus()
        self.btn = tk.Button(self.root,
                            text="Click here to copy image to your clipboard",
                            font="100",
                            bg="green",
                            fg="white",
                            compound=tk.CENTER,
                            command=self.CopyToClipboard)
        self.label.place(width=600, height=300)
        self.ent.place(y=300, width=600, height=150)
        # self.ent.pack(side=tk.LEFT)
        self.btn.place(y=450, width=600, height=250)
        # self.btn.pack(side=tk.RIGHT)

        self.root.bind('<Return>', self.CallbackEnter)
        self.root.mainloop()

    def CallbackEnter(self, event):
        self.CopyToClipboard()

    def CopyToClipboard(self):
        try:
            img_path = BASEPATH + "\\images\\" + self.ent.get()
            ctc.copy_to_clipboard(img_path)
            self.ent.delete(0, 'end')
        except:
            print("CopyToClipboard Error!!")

if __name__ == "__main__":
    try:
        ctc_app = app()
    except Exception:
        print(Exception.args)
