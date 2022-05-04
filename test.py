from datetime import datetime
import turtle as t
from time import sleep

def marcas(t, posx, posy,raio):
    t.pu()
    t.goto(posx,posy)
    t.color("gray")
    for i in range(60):
        if i % 5 == 0:
            d = 0.2
            w = 4
        else:
            d = 0.1
            w = 2
        t.fd(raio*(1 - d))
        t.pd()
        t.fd(raio*d)
        t.pu()
        t.bk(raio)
        t.rt(6)
        

def ponteiro(t, posx, posy, raio, ang):
    t.pu()
    t.goto(posx, posy)
    t.color("purple")
    t.width(2)
    t.seth(90 - ang)
    t.pd()
    t.fd(raio)
    
def ponteiroM(t, posx, posy, raio, ang):
    t.pu()
    t.goto(posx, posy)
    t.color("black")
    t.width(3)
    t.seth(90 - ang)
    t.pd()
    t.fd(raio)
    
def ponteiroH(t, posx, posy, raioH, ang):
    t.pu()
    t.goto(posx, posy)
    t.color("black")
    t.width(7)
    t.seth(90 - ang)
    t.pd()
    t.fd(raioH)
    
   

t.tracer(0)         

x = 0
y = 0
r = 200

while True:
    now = datetime.now()
    s_ang = now.second * 6 + now.microsecond / 1000000 * 6
    s_angM = now.minute * 6 + now.minute * 0.1
    s_angH = now.hour * 30 + now.minute * 0.5
    t.reset()
    raioH= 150
    marcas(t,x,y,r)
    ponteiro(t, x, y, r, s_ang)
    ponteiroM(t, x, y, r, s_angM)
    ponteiroH(t, x, y, raioH, s_angH)
    t.update()
    


