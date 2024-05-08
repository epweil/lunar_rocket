
import turtle
import time
class lunar_module():
        
        

        def __init__(self, mass = 1):
                self.obj = turtle.Turtle()
                self.obj.shape('square')
                self.obj.color('black')
                self.forces_left =0
                self.forces_right =0
                self.forces_up =0
                self.mass = mass
                self.forces_vert = 0
                self.velocity_vert = 0
                self.blaster =False

        def move(self,t=0.1):
                self.forces_vert = (-9.8 + (100*self.blaster))*self.mass
                velocity_vert_delta = t* self.forces_vert/self.mass
                self.velocity_vert += velocity_vert_delta
                delta = self.velocity_vert*t + 0.5*self.forces_vert*(t**2)/self.mass
                print(self.velocity_vert)
                self.obj.sety(self.obj.ycor() + delta)
                
        

        def blaster_on(self):
                self.blaster = True
        def blaster_off(self):
                 self.blaster = False

window = turtle.Screen()
window.bgcolor('white')
rocket = lunar_module()



window.onkeypress(rocket.blaster_on, "Up")
window.onkeyrelease(rocket.blaster_off, "Up")
window.listen()
while True:
        rocket.move()
        window.update()
        time.sleep(0.02)
