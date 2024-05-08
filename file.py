
import turtle
import time
import math
import random 
class lunar_module():
        
        

        def __init__(self, mass = 1):
                self.obj = turtle.Turtle()
                self.obj.penup()
                self.obj.shape('square')
                self.obj.color('black')
                self.mass = mass
                self.velocity_hori = 0
                self.velocity_vert = 0
                self.force_hori = 0
                self.force_vert = 0
                self.blaster =False


                ##TEXT DISPLAYES
                self.textPos = turtle.Turtle(visible=False)
                self.textPos.penup()
                self.textPos.goto(250,310)
                
                self.textPos.color("black")
                

                self.textVelo = turtle.Turtle(visible=False)
                self.textVelo.penup()
                self.textVelo.goto(250,300)
                self.textVelo.color("black")
                
        def move(self,t=0.05):

                angle_delta = -self.obj.heading()
                
                hori_multiple = math.sin(math.pi*angle_delta/180)
                vert_multiple = math.cos(math.pi*angle_delta/180)

                force_blaster = (self.blaster*50)*self.mass

                self.force_vert = (force_blaster * vert_multiple) -9.8
                self.force_hori = force_blaster * hori_multiple

                velocity_vert_delta = t* self.force_vert/self.mass
                velocity_hori_delta = t* self.force_hori/self.mass

                self.velocity_vert += velocity_vert_delta
                self.velocity_hori += velocity_hori_delta

                delta_vert = self.velocity_vert*t + 0.5*self.force_vert*(t**2)/self.mass
                delta_hori = self.velocity_hori*t + 0.5*self.force_hori*(t**2)/self.mass

                self.obj.sety(self.obj.ycor() + delta_vert)
                self.obj.setx(self.obj.xcor() + delta_hori)
                self.textPos.undo()
                self.textPos.write("Position: (" + str(round(self.obj.xcor(),2)) + ","+ str(round(self.obj.ycor(),2)) + ")",  font=('Arial', 10, 'normal'))
                self.textVelo.undo()
                self.textVelo.write("Velocty: (" + str(round(self.velocity_hori,2)) + ","+ str(round(self.velocity_vert,2)) + ")",  font=('Arial', 10, 'normal'))
                
                # self.text.goto(0,100)
                # self.text.write("Position Y " + str(self.obj.xcor()), move=False, align='center', font=('Arial', 20, 'normal'))

        def blaster_on(self):
                self.blaster = True
        def blaster_off(self):
                 self.blaster = False
        
        def turn_left(self):
                self.obj.left(5)
        def turn_right(self):
                angle_delta = self.obj.heading()
                hori_multiple = math.sin(math.pi*angle_delta/180)
                print(hori_multiple)
                self.obj.right(5)
        def reset(self):
                 print("RESET")
                 self.obj.setheading(0)
                 self.obj.sety(0)
                 self.obj.setx(0)
                 self.velocity_hori =0
                 self.velocity_vert =0


class landing_pad():
        def __init__(self):
                rand_hori_left = random.random() * 250 -30
                rand_vert = random.random() * 250 +30
                
                self.obj = turtle.Turtle(visible=False)
                self.obj.color("RED")
                self.obj.penup()
                self.obj.goto(rand_hori_left,rand_vert)
                self.obj.pensize(4)
                self.obj.pendown()
                self.obj.goto(rand_hori_left,rand_vert-10)
                self.obj.goto(rand_hori_left+100,rand_vert-10)
                self.obj.goto(rand_hori_left+100,rand_vert)
                self.obj.penup()


window = turtle.Screen()
window.bgcolor('white')
rocket = lunar_module()
landing = landing_pad()



window.onkeypress(rocket.blaster_on, "Up")
window.onkeypress(rocket.turn_right, "Right")
window.onkeypress(rocket.turn_left, "Left")
window.onkeyrelease(rocket.blaster_off, "Up")
window.onkeypress(rocket.reset, "space")

window.listen()

while True:
        rocket.move()
        window.update()
        time.sleep(0.001)
