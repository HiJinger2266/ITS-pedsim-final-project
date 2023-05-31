from tkinter import *
import numpy as np
import time
import datetime
import agent
import socialforce

agents = []
dots = []

def AgentCreater():
    x0 = np.random.uniform(200,250)
    y0 = np.random.uniform(100,150)
    x1 = np.random.uniform(400,450)
    y1 = np.random.uniform(250,300)
    agents.append(agent.Agent(startpoint=[x0,y0],endpoint=[x1,y1]))
    dots.append(canva.create_oval(agents[-1].position_vec[0]-5,agents[-1].position_vec[1]-5,
                                  agents[-1].position_vec[0]+5,agents[-1].position_vec[1]+5, fill="black"))
        
def MoveOneStep(e):
    for j in range(len(agents)):
        agents[j].update()
        canva.moveto(dots[j], agents[j].position_vec[0], agents[j].position_vec[1])
        if agents[j].check_arrival() == True:
            canva.delete(dots[j])
    for i in range(len(agents)):
        if agents[i].check_arrival() == True:
            del dots[i]
            del agents[i]

window = Tk()
window.title("Test Agent")
window.geometry("800x600")

texting = Label(window, text="Test Agent", font=("Candara", 20))
texting.pack()

canva = Canvas(window, width=600, height=400)
canva.pack()
canva.configure(bg="gray")

btncreate = Button(window, text="Add a tourist!", command=AgentCreater, font=("Candara", 16), bg='yellow')
btncreate.pack()

btnmove = Button(window, text="Move 1 step", command=MoveOneStep, font=("Candara", 16), bg='yellow')
btnmove.pack()
window.bind("<space>", MoveOneStep)

window.mainloop()


