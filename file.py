
import turtle
import time
import math
class lunar_module():
        
        

        def __init__(self, mass = 1):
                self.obj = turtle.Turtle()
                self.obj.shape('square')
                self.obj.color('black')
                self.mass = mass
                self.velocity_hori = 0
                self.velocity_vert = 0
                self.force_hori = 0
                self.force_vert = 0
                self.blaster =False

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

window = turtle.Screen()
window.bgcolor('white')
rocket = lunar_module()



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
