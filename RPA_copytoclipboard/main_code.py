import tkinter as tk
import copy_to_clipboard as ctc
import os

BASEPATH = os.path.dirname(os.path.realpath(__file__))

class app(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Copy Image to Clipboard")

        # UI
        self.root.geometry("600x400+1000+500")
        self.root.resizable(False, False)
        self.ent = tk.Entry(self.root, font="100")
        self.ent.focus()
        self.btn = tk.Button(self.root,
                            text="Click here to copy image to your clipboard",
                            font="100",
                            bg="green",
                            fg="white",
                            compound=tk.CENTER,
                            command=self.CopyToClipboard)
        self.ent.place(width=600, height=150)
        # self.ent.pack(side=tk.LEFT)
        self.btn.place(y=200, width=600, height=250)
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
