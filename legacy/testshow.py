from tkinter import *
import time
import datetime
import agent
import socialforce

agents = []
dots = []

def AgentCreater():
    agents.append(agent.Agent(startpoint=[18,30],endpoint=[425,66]))
    dots.append(canva.create_oval(agents[-1].position_vec[0]-5,agents[-1].position_vec[1]-5,
                                  agents[-1].position_vec[0]+5,agents[-1].position_vec[1]+5, fill="black"))
        
def MoveOneStep(e):
    for i in range(len(agents)):
        agents[i].update()
    for j in range(len(agents)):
        canva.moveto(dots[j], agents[j].position_vec[0], agents[j].position_vec[1])
        if agents[j].check_arrival() == True:
            del dots[j]
            del agents[j]

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


