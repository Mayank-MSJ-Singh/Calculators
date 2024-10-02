from tkinter import *
ev = '0+'
try:
  #while 1<2:
  a = Tk(className = " Keyboard")
  a.geometry("0x100")
  def one():
    global ev
    ev = ev + '1'
  def two():
     global ev
     ev = ev + '2'
  def three():
     global ev
     ev = ev + '3'
  def four():
     global ev
     ev = ev + '4'
  def five():
     global ev
     ev = ev + '5'
  def six():
     global ev
     ev = ev + '6'
#     on = 1
  def seven():
     global ev
     ev = ev + '7'
#     on = 1
  def eight():
     global ev
     ev = ev + '8'
#     on = 1
  def nine():
     global ev
     ev = ev + '9'
#     on = 1
  def zero():
     global ev
     ev = ev + '0'
#     on = 1
  def plus():
     global ev
     ev = ev + '+'
#     on = 1
  def minus():
     global ev
     ev = ev + '-'
#     on = 1
  def divide():
     global ev
     ev = ev + '/'
  def multiply():
     global ev
     ev = ev + '*'
  def enter():
      global ev
      try:
          print(eval(ev))
      except:
          print(0)
      ev = "0+"
  b = Button(a,text = "1", command = one)
  c = Button(a,text = "2", command = two)
  d = Button(a,text = "3", command = three)
  e = Button(a,text = "4", command = four)
  f = Button(a,text = "5", command = five)
  g = Button(a,text = "6", command = six)
  h = Button(a,text = "7", command = seven)
  i = Button(a,text = "8", command = eight)
  j = Button(a,text = "9", command = nine)
  k = Button(a,text = "0", command = zero)
  l = Button(a,text = "-", command = minus)
  m = Button(a,text = "/", command = divide)
  n = Button(a,text = "*", command = multiply)
  o = Button(a,text = "+", command = plus)
  p = Button(a, text="Enter", command=enter)
  p.grid()
  q = Button(a,text ="Close", command = exit)
  b.grid(row=1, column=1)
  c.grid(row=1, column=2)
  d.grid(row=1, column=3)
  e.grid(row=2, column=1)
  f.grid(row=2, column=2)
  g.grid(row=2, column=3)
  h.grid(row=3, column=1)
  i.grid(row=3, column=2)
  j.grid(row=3, column=3)
  k.grid(row=4, column=2)
  l.grid(row=1, column=4)
  m.grid(row=2, column=4)
  n.grid(row=3, column=4)
  o.grid(row=4, column=4)
  p.grid(row=1, column=5)
  q.grid(row=2, column=5)
  a.mainloop()
except:
    print(0)