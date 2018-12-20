import tkinter.filedialog as dialog
import tkinter as tk

atgc = []; new_label = ''
window = tk.Tk()
text = tk.Text(window, width=50, height=20)

newframe = tk.Frame(window)
label = tk.Label(newframe, textvariable=new_label)
newframe.grid(row=2, columnspan=2)

def readFile():
  global atgc, new_label, label
  afile = dialog.askopenfile(mode='rb',title='Choose a file')

  atgc = [0,0,0,0]
  data = []
  for k in afile:
    for j in k:
      i = chr(j)
      data.append(i)
      if i == "A":
        atgc[0] += 1
      elif i == "T":
        atgc[1] += 1
      elif i == "G":
        atgc[2] += 1
      elif i == "C":
        atgc[3] += 1

  new_label = "I got {} bytes from this file.".format(sum(atgc))
  text.insert('0.0', ''.join(data))
  label.config(text = new_label)

def count():
  global atgc, new_label, label
  new_label = "Num As: {}  Num Ts: {}  Num Gs: {}  Num Cs: {}  ".format(atgc[0], atgc[1], atgc[2], atgc[3])
  label.config(text = new_label)

def main():
  global new_label, label, frame

  text.grid(row=0, columnspan=2)

  readFileButton = tk.Button(window, text="Read a File", command=readFile)
  readFileButton.grid(row=1, column=0)

  countButton = tk.Button(window, text="Count", command=count)
  countButton.grid(row=1, column=1)

  label.pack()

  window.mainloop()


if __name__ == '__main__':
  main()
