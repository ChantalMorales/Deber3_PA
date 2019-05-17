from tkinter import*
from tkinter import messagebox
tk=Tk()

x=0
y=0
canvas=Canvas(tk,width=960,height=680)
canvas.pack()
pelota=PhotoImage(file='pelota.gif')
cancha=PhotoImage(file='estadio.gif')

canvas.create_image(0,0,anchor=NW, image=cancha)
canvas.create_image(80,150,anchor=CENTER, image=pelota)


def moverpelota(event):
    global y,x
    if event.keysym=='Up':
        
        canvas.move(2,0,-6)
        y=y-6
    elif event.keysym=='Down':
        
        
        canvas.move(2,0,6)
        y=y+6
    elif event.keysym=='Left':
        
        canvas.move(2,-6,0)
        x=x-6
    else:        
        canvas.move(2,6,0)

        x=x+6
    if x==762 or x==-36:
        messagebox.showinfo(message="HAS ANOTADO UN GOOOOOOOL!", title="Fútbol")

    
    
canvas.bind_all('<KeyPress-Up>',moverpelota)
canvas.bind_all('<KeyPress-Down>',moverpelota)
canvas.bind_all('<KeyPress-Left>',moverpelota)
canvas.bind_all('<KeyPress-Right>',moverpelota)



tk.mainloop()
