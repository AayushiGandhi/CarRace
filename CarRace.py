from tkinter import *
import tkinter as tk
import tkinter.ttk
from PIL import ImageTk, Image
from tkinter import font as tkfont
from random import randrange
import time
import random
import threading
from tkinter.messagebox import showinfo


canvas_height = 680
canvas_width = 780
flag = 0

def raise_frame(frame):
    frame.tkraise()

root = Tk()
title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

f1 = Frame(root) #mainpage
f2 = Frame(root) #singleplayer
f3 = Frame(root) #multiplayer
for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')

x1 = Frame(root)
x2 = Frame(root)
x3 = Frame(root)
x4 = Frame(root)
for frame in (x1, x2, x3, x4):
    frame.grid(row=0, column=0)


#win = Frame(root) Winning frame

f1.tkraise()
#---------------------------Main page------------------------------------------------------
Label(f1, text='Welcome to car race',font=title_font).pack()

c = tk.Canvas(f1,width = canvas_width, height = canvas_height)
main_img = ImageTk.PhotoImage(Image.open("main.jpg"))
c.create_image(0,0,anchor=NW,image=main_img)
c.pack()
Button(f1, text='Single player', command=lambda:raise_frame1(f2)).pack()
Button(f1, text='Multiplayer', command=lambda:raise_frame(f3)).pack()

#---------------------------Single player page----------------------------------------------
Label(f2, text='Single Player',font=title_font).pack()

canvas = tk.Canvas(f2, width = canvas_width, height = canvas_height, bg = "green")
canvas.pack()

y = canvas_height - 80
#Grid
canvas.create_line(389,0,389,y)
canvas.pack()

#for i in range(6):
canvas.create_line(0,100*(5+1),canvas_width,100*(5+1)) 
canvas.pack()

#Place cars
def single_1():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas.move(item_single1, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t1_1 = canvas.bbox(item_single1)
    if t1_1[1] < 514 and t1_1[3]< 616:
        root.after(7, single_1)
    #print(canvas1.bbox(item_two1))

    
    if str(canvas.bbox(item_single1)) == "(154, 514, 234, 616)" and flag == 0:
        flag = 1
        top1_1 = Toplevel()
        top1_1.geometry('309x225')
        top1_1.title('Car race results')
        l1_1 = Label(top1_1, text = 'Winner is car 1')
        l1_1.pack()
        Button(top1_1, text='Exit', command=lambda:root.destroy()).pack()

def single_2(event):
    global flag
    #print(event.keysym)
    canvas.move(item_single2, 0, random.uniform(0,1.5))
    #print(canvas.bbox(item_single2))

    if str(canvas.bbox(item_single2)) == "(547, 525, 617, 616)" and flag == 0:
        flag = 1
        top1_2 = Toplevel()
        top1_2.geometry('309x225')
        top1_2.title('Car race results')
        l1_2 = Label(top1_2, text = 'Winner is car 2')
        l1_2.pack()
        Button(top1_2, text='Exit', command=lambda:root.destroy()).pack()

image_single1 = "r1.png"
photo_single1 = PhotoImage(file=image_single1)
item_single1 = canvas.create_image(194, 50, image=photo_single1) 
#root.bind('<KeyPress-Down>', single_1)

image_single2 = "b1.png"
photo_single2 = PhotoImage(file=image_single2)
item_single2 = canvas.create_image(582,50, image=photo_single2) 


def raise_frame1(f2):
    f2.tkraise()
    single_1()
    root.bind('<KeyPress-Down>', single_2)

    
#finishing line
#canvas.create_line(0,y,canvas_width,y)
#canvas.pack()

img = Image.open('flag.jpg')
canvas_image = ImageTk.PhotoImage(img)
canvas.create_image(canvas_width//2, y+40, image=canvas_image)
canvas.pack()

Button(f2, text='Return to main menu', command=lambda:raise_frame(f1)).pack()

#---------------------------Multiplayer page----------------------------------------------
Label(f3, text='Multiplayer',font=title_font).grid(row=0,column=0)

Button(f3, text='Two player', command=lambda:raise_frame2(x1)).grid(row=1,column=0)
Button(f3, text='Three player', command=lambda:raise_frame3(x2)).grid(row=2,column=0)
Button(f3, text='Four player', command=lambda:raise_frame4(x3)).grid(row=3,column=0)
Button(f3, text='Five player', command=lambda:raise_frame5(x4)).grid(row=4,column=0)
Button(f3, text='Return to main menu', command=lambda:raise_frame(f1)).grid(row=5,column=0)
#---------------------------Two player page-----------------------------------------------
Label(x1, text='Two Player',font=title_font).pack()
canvas1 = tk.Canvas(x1, width = canvas_width, height = canvas_height, bg = "green")
canvas1.pack()

y = canvas_height - 80
#Grid
canvas1.create_line(389,0,389,y)
canvas1.pack()

#for i in range(6):
canvas1.create_line(0,100*(5+1),canvas_width,100*(5+1)) 
canvas1.pack()

#Place cars
def two_1():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas1.move(item_two1, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t2_1 = canvas1.bbox(item_two1)
    if t2_1[1] < 514 and t2_1[3]< 616:
        root.after(7, two_1)
    #print(canvas1.bbox(item_two1))

    
    if str(canvas1.bbox(item_two1)) == "(154, 514, 234, 616)" and flag == 0:
        flag = 1
        top2_1 = Toplevel()
        top2_1.geometry('309x225')
        top2_1.title('Car race results')
        l2_1 = Label(top2_1, text = 'Winner is car 1')
        l2_1.pack()
        Button(top2_1, text='Exit', command=lambda:root.destroy()).pack()

def two_2():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas1.move(item_two2, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t2_2 = canvas1.bbox(item_two2)
    if t2_2[1] < 525 and t2_2[3]< 616:
        root.after(7, two_2)
    #print(canvas1.bbox(item_two2))

    
    if str(canvas1.bbox(item_two2)) == "(547, 525, 617, 616)" and flag == 0:
        flag = 1
        top2_2 = Toplevel()
        top2_2.geometry('309x225')
        top2_2.title('Car race results')
        l2_2 = Label(top2_2, text = 'Winner is car 2')
        l2_2.pack()
        Button(top2_2, text='Exit', command=lambda:root.destroy()).pack()

image_two1 = "r1.png"
photo_two1 = PhotoImage(file=image_two1)
item_two1 = canvas1.create_image(194, 50, image=photo_two1) 
#root.bind('<KeyPress-Down>', two_1)

image_two2 = "b1.png"
photo_two2 = PhotoImage(file=image_two2)
item_two2 = canvas1.create_image(582,50, image=photo_two2) 
#root.bind('<KeyPress-Down>', two_2)

def raise_frame2(x1):
    x1.tkraise()

    # creating threads 
    t1 = threading.Thread(target=two_1) 
    t2 = threading.Thread(target=two_2)
      
    # start threads 
    t1.start() 
    t2.start()

#finishing line
#y = canvas_height - 80
#canvas1.create_line(0,y,canvas_width,y)
#canvas1.pack()

img1 =Image.open('flag.jpg')
canvas_image1 = ImageTk.PhotoImage(img1)
canvas1.create_image(canvas_width//2, y+40, image=canvas_image)
canvas1.pack()


Button(x1, text='Return to main menu', command=lambda:raise_frame(f1)).pack()

#---------------------------Three player page----------------------------------------------
Label(x2, text='Three Player',font=title_font).pack()
canvas2 = tk.Canvas(x2, width = canvas_width, height = canvas_height, bg = "green")
canvas2.pack()

y = canvas_height - 80
#Grid
canvas2.create_line(259,0,259,y)
canvas2.pack()
canvas2.create_line(518,0,518,y)
canvas2.pack()

#for i in range(6):
canvas2.create_line(0,100*(5+1),canvas_width,100*(5+1)) 
canvas2.pack()

#Place cars
def three_1():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas2.move(item_three1, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t3_1 = canvas2.bbox(item_three1)
    if t3_1[1] < 514 and t3_1[3]< 616:
        root.after(7, three_1)
    #print(canvas2.bbox(item_three1))

    
    if str(canvas2.bbox(item_three1)) == "(89, 514, 169, 616)" and flag == 0:
        flag = 1
        top3_1 = Toplevel()
        top3_1.geometry('309x225')
        top3_1.title('Car race results')
        l3_1 = Label(top3_1, text = 'Winner is car 1')
        l3_1.pack()
        Button(top3_1, text='Exit', command=lambda:root.destroy()).pack()

def three_2():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas2.move(item_three2, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t3_2 = canvas2.bbox(item_three2)
    if t3_2[1] < 525 and t3_2[3]< 616:
        root.after(7, three_2)
    #print(canvas2.bbox(item_three2))

    
    if str(canvas2.bbox(item_three2)) == "(352, 525, 422, 616)" and flag == 0:
        flag = 1
        top3_2 = Toplevel()
        top3_2.geometry('309x225')
        top3_2.title('Car race results')
        l3_2 = Label(top3_2, text = 'Winner is car 2')
        l3_2.pack()
        Button(top3_2, text='Exit', command=lambda:root.destroy()).pack()


def three_3():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas2.move(item_three3, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t3_3 = canvas2.bbox(item_three3)
    if t3_3[1] < 514 and t3_3[3]< 616:
        root.after(7, three_3)
    #print(canvas2.bbox(item_three3))

    
    if str(canvas2.bbox(item_three3)) == "(605, 514, 685, 616)" and flag == 0:
        flag = 1
        top3_3 = Toplevel()
        top3_3.geometry('309x225')
        top3_3.title('Car race results')
        l3_3 = Label(top3_3, text = 'Winner is car 3')
        l3_3.pack()
        Button(top3_3, text='Exit', command=lambda:root.destroy()).pack()

    
image_three1 = "r1.png"
photo_three1 = PhotoImage(file=image_three1)
item_three1 = canvas2.create_image(129, 50, image=photo_three1) 
#root.bind('<KeyPress-Down>', three_1)

image_three2 = "b1.png"
photo_three2 = PhotoImage(file=image_three2)
item_three2 = canvas2.create_image(387,50, image=photo_three2) 
#root.bind('<KeyPress-Down>', three_2)

image_three3 = "r2.png"
photo_three3 = PhotoImage(file=image_three3)
item_three3 = canvas2.create_image(645,50, image=photo_three3) 
#root.bind('<KeyPress-Down>', three_3)


def raise_frame3(x2):
    x2.tkraise()

    # creating threads 
    t1 = threading.Thread(target=three_1) 
    t2 = threading.Thread(target=three_2)
    t3 = threading.Thread(target=three_3) 
      
    # start threads 
    t1.start() 
    t2.start()
    t3.start() 
    
#finishing line
#y = canvas_height - 80
#canvas2.create_line(0,y,canvas_width,y)
#canvas2.pack()

img2 =Image.open('flag.jpg')
canvas_image2 = ImageTk.PhotoImage(img2)
canvas2.create_image(canvas_width//2, y+40, image=canvas_image2)
canvas2.pack()

Button(x2, text='Return to main menu', command=lambda:raise_frame(f1)).pack()
#---------------------------Four player page----------------------------------------------
Label(x3, text='Four Player',font=title_font).pack()
canvas3 = tk.Canvas(x3, width = canvas_width, height = canvas_height, bg = "green")
canvas3.pack()

canvas3.create_line(194,0,194,y)
canvas3.pack()
canvas3.create_line(388,0,388,y)
canvas3.pack()
canvas3.create_line(582,0,582,y)
canvas3.pack()

#for i in range(6):
canvas3.create_line(0,100*(5+1),canvas_width,100*(5+1)) 
canvas3.pack()

#Place cars
def four_1():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas3.move(item_four1, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t4_1 = canvas3.bbox(item_four1)
    if t4_1[1] < 515 and t4_1[3]< 617:
        root.after(7, four_1)
    #print(canvas3.bbox(item_four1))

    
    if str(canvas3.bbox(item_four1)) == "(57, 515, 137, 617)" and flag == 0:
        flag = 1
        top4_1 = Toplevel()
        top4_1.geometry('309x225')
        top4_1.title('Car race results')
        l4_1 = Label(top4_1, text = 'Winner is car 1')
        l4_1.pack()
        Button(top4_1, text='Exit', command=lambda:root.destroy()).pack()

def four_2():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas3.move(item_four2, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t4_2 = canvas3.bbox(item_four2)
    if t4_2[1] < 526 and t4_2[3]< 617:
        root.after(7, four_2)
    #print(canvas3.bbox(item_four2))

    
    if str(canvas3.bbox(item_four2)) == "(256, 526, 326, 617)" and flag == 0:
        flag = 1
        top4_2 = Toplevel()
        top4_2.geometry('309x225')
        top4_2.title('Car race results')
        l4_2 = Label(top4_2, text = 'Winner is car 2')
        l4_2.pack()
        Button(top4_2, text='Exit', command=lambda:root.destroy()).pack()

def four_3():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas3.move(item_four3, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t4_3 = canvas3.bbox(item_four3)
    if t4_3[1] < 515 and t4_3[3]< 617:
        root.after(7, four_3)
    #print(canvas3.bbox(item_four3))

    
    if str(canvas3.bbox(item_four3)) == "(445, 515, 525, 617)" and flag == 0:
        flag = 1
        top4_3 = Toplevel()
        top4_3.geometry('309x225')
        top4_3.title('Car race results')
        l4_3 = Label(top4_3, text = 'Winner is car 3')
        l4_3.pack()
        Button(top4_3, text='Exit', command=lambda:root.destroy()).pack()

def four_4():
    global flag
    #print(event.keysym)
    #canvas3.move(item_four1, 0, 100)
    canvas3.move(item_four4, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), four_1)

    t4_4 = canvas3.bbox(item_four4)
    if t4_4[1] < 525 and t4_4[3]< 616:
        root.after(7, four_4)
    #print(canvas3.bbox(item_four4))

    
    if str(canvas3.bbox(item_four4)) == "(644, 525, 714, 616)" and flag == 0:
        flag = 1
        top4_4 = Toplevel()
        top4_4.geometry('309x225')
        top4_4.title('Car race results')
        l4_4 = Label(top4_4, text = 'Winner is car 4')
        l4_4.pack()
        Button(top4_4, text='Exit', command=lambda:root.destroy()).pack()

    
image_four1 = "r1.png"
photo_four1 = PhotoImage(file=image_four1)
item_four1 = canvas3.create_image(97, 50, image=photo_four1) 
#root.bind('<KeyPress-Down>', four_1)

image_four2 = "b1.png"
photo_four2 = PhotoImage(file=image_four2)
item_four2 = canvas3.create_image(291,50, image=photo_four2) 
#root.bind('<KeyPress-Down>', four_2)

image_four3 = "r2.png"
photo_four3 = PhotoImage(file=image_four3)
item_four3 = canvas3.create_image(485,50, image=photo_four3) 
#root.bind('<KeyPress-Down>', four_3)

image_four4 = "b2.png"
photo_four4 = PhotoImage(file=image_four4)
item_four4 = canvas3.create_image(679,50, image=photo_four4) 
#root.bind('<KeyPress-Down>', four_4)

def raise_frame4(x3):
    x3.tkraise()

    # creating threads 
    t1 = threading.Thread(target=four_1) 
    t2 = threading.Thread(target=four_2)
    t3 = threading.Thread(target=four_3) 
    t4 = threading.Thread(target=four_4) 
      
    # start threads 
    t1.start() 
    t2.start()
    t3.start() 
    t4.start()


#finishing line
#y = canvas_height - 80
#canvas3.create_line(0,y,canvas_width,y)
#canvas3.pack()

img3 =Image.open('flag.jpg')
canvas_image3 = ImageTk.PhotoImage(img3)
canvas3.create_image(canvas_width//2, y+40, image=canvas_image3)
canvas3.pack()

Button(x3, text='Return to main menu', command=lambda:raise_frame(f1)).pack()
#---------------------------Five player page----------------------------------------------

Label(x4, text='Five Player',font=title_font).pack()
canvas4 = tk.Canvas(x4, width = canvas_width, height = canvas_height, bg = "green")
canvas4.pack()

canvas4.create_line(155,0,155,y)
canvas4.pack()
canvas4.create_line(310,0,310,y)
canvas4.pack()
canvas4.create_line(465,0,465,y)
canvas4.pack()
canvas4.create_line(620,0,620,y)
canvas4.pack()
    

#for i in range(6):
#canvas4.create_line(0,100*(i+1),canvas_width,100*(i+1)) 
#canvas4.pack()

#Finishing line
canvas4.create_line(0,100*(5+1),canvas_width,100*(5+1)) 
canvas4.pack()

image_five1 = "r1.png"
photo_five1 = PhotoImage(file=image_five1)
item_five1 = canvas4.create_image(77, 50, image=photo_five1)
#root.bind('<KeyPress-Down>', five_1)

image_five2 = "b1.png"
photo_five2 = PhotoImage(file=image_five2)
item_five2 = canvas4.create_image(231,50, image=photo_five2) 
#root.bind('<KeyPress-Down>', five_2)

image_five3 = "r2.png"
photo_five3 = PhotoImage(file=image_five3)
item_five3 = canvas4.create_image(385,50, image=photo_five3) 
#root.bind('<KeyPress-Down>', five_3)

image_five4 = "b2.png"
photo_five4 = PhotoImage(file=image_five4)
item_five4 = canvas4.create_image(539,50, image=photo_five4) 
#root.bind('<KeyPress-Down>', five_4)

image_five5 = "r3.png"
photo_five5 = PhotoImage(file=image_five5)
item_five5 = canvas4.create_image(693,50, image=photo_five5)
#root.bind('<KeyPress-Down>', five_5)

        
m = (0,100*(5+1),canvas_width,100*(5+1))
#Place cars
def five_1():
    global flag
    #print(event.keysym)
    #canvas4.move(item_five1, 0, random.randint(1, y))
    canvas4.move(item_five1, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)

    t = canvas4.bbox(item_five1)
    if t[1] < 526 and t[3]< 628:
        root.after(7, five_1)
    #print(type(canvas4.bbox(item_five1)))

    
    if str(canvas4.bbox(item_five1)) == "(37, 526, 117, 628)" and flag == 0:
        flag = 1
        top = Toplevel()
        top.geometry('309x225')
        top.title('Car race results')
        label99 = Label(top, text = 'Winner is car 1')
        label99.pack()
        #root.withdraw()
        #win = Toplevel(root, width = canvas_width, height = canvas_height, bg = "green")
        #Label(win, text='Winner car 1',font=title_font).pack()
        #canvas55 = tk.Canvas(win, width = canvas_width, height = canvas_height, bg = "green")
        #canvas55.pack()
        Button(top, text='Exit', command=lambda:root.destroy()).pack()
        #win.wm_title("Winner is car 1")
        
        
def five_2():
    global flag
    #print(event.keysym)
    #canvas4.move(item_five2, 0, random.randint(1, y))
    canvas4.move(item_five2, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), five_2)

    t2 = canvas4.bbox(item_five2)
    if t2[1] < 537 and t2[3] < 628:
        root.after(7, five_2)
    #print(type(canvas4.bbox(item_five1)))

    #print(canvas4.bbox(item_five2))
    if str(canvas4.bbox(item_five2)) == "(196, 537, 266, 628)" and flag == 0:
        flag = 1
        top2 = Toplevel()
        top2.geometry('309x225')
        top2.title('Car race results')
        l2 = Label(top2, text = 'Winner is car 2')
        l2.pack()
        #root.withdraw()
        #win = Toplevel(root, width = canvas_width, height = canvas_height, bg = "green")
        #Label(win, text='Winner car 1',font=title_font).pack()
        #canvas55 = tk.Canvas(win, width = canvas_width, height = canvas_height, bg = "green")
        #canvas55.pack()
        Button(top2, text='Exit', command=lambda:root.destroy()).pack()
        #win.wm_title("Winner is car 1")

def five_3():
    global flag
    #print(event.keysym)
    #canvas4.move(item_five3, 0, random.randint(1, y))
    canvas4.move(item_five3, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    

    t3 = canvas4.bbox(item_five3)
    if t3[1] < 526 and t3[3] < 628:
        root.after(7, five_3)
    #print(type(canvas4.bbox(item_five1)))

    #print(canvas4.bbox(item_five3))
    if str(canvas4.bbox(item_five3)) == "(345, 526, 425, 628)" and flag == 0:
        flag = 1
        top3 = Toplevel()
        top3.geometry('309x225')
        top3.title('Car race results')
        l3 = Label(top3, text = 'Winner is car 3')
        l3.pack()
        #root.withdraw()
        #win = Toplevel(root, width = canvas_width, height = canvas_height, bg = "green")
        #Label(win, text='Winner car 1',font=title_font).pack()
        #canvas55 = tk.Canvas(win, width = canvas_width, height = canvas_height, bg = "green")
        #canvas55.pack()
        Button(top3, text='Exit', command=lambda:root.destroy()).pack()
        #win.wm_title("Winner is car 1")


def five_4():
    global flag
    #print(event.keysym)
    #canvas4.move(item_five4, 0, random.randint(1, y))
    canvas4.move(item_five4, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    
    t4 = canvas4.bbox(item_five4)
    if t4[1] < 537 and t4[3] < 628:
        root.after(7, five_4)

    #print(canvas4.bbox(item_five4))
    if str(canvas4.bbox(item_five4)) == "(504, 537, 574, 628)" and flag == 0:
        #print("--------------------------------------------------------")
        flag = 1
        top4 = Toplevel()
        top4.geometry('309x225')
        top4.title('Car race results')
        l4 = Label(top4, text = 'Winner is car 4')
        l4.pack()
        #root.withdraw()
        Button(top4, text='Exit', command=lambda:root.destroy()).pack()


def five_5():
    global flag
    #print(event.keysym)
    #canvas4.move(item_five5, 0, random.randint(20, 50))
    canvas4.move(item_five5, 0, random.uniform(0,1))
    # move again after 25ms (0.025s)
    #root.after(random.randint(1,30), five_5)

    t5 = canvas4.bbox(item_five5)
    if t5[1] < 526 and t5[3] < 628:
        root.after(9, five_5)

    #print(canvas4.bbox(item_five5))
    if str(canvas4.bbox(item_five5)) == "(653, 526, 733, 628)" and flag == 0:
        #print("--------------------------------------------------------")
        flag = 1
        top5 = Toplevel()
        top5.geometry('309x225')
        top5.title('Car race results')
        l5 = Label(top5, text = 'Winner is car 5')
        l5.pack()
        #root.withdraw()
        Button(top5, text='Exit', command=lambda:root.destroy()).pack()


def raise_frame5(x4):
    x4.tkraise()

    # creating threads 
    t1 = threading.Thread(target=five_1) 
    t2 = threading.Thread(target=five_2)
    t3 = threading.Thread(target=five_3) 
    t4 = threading.Thread(target=five_4)
    t5 = threading.Thread(target=five_5) 
      
    # start threads 
    t1.start() 
    t2.start()
    t3.start() 
    t4.start()
    t5.start()

    five_1()    
    five_2()
    five_3()
    five_4()
    five_5()
            

#finishing line
#y = canvas_height - 80
#canvas4.create_line(0,y,canvas_width,y)
#canvas4.pack()

img4 =Image.open('flag.jpg')
canvas_image4 = ImageTk.PhotoImage(img4)
canvas4.create_image(canvas_width//2, y+40, image=canvas_image4)
canvas4.pack()
        
Button(x4, text='Return to main menu', command=lambda:raise_frame(f1)).pack()


root.mainloop()
