from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


#defines what a ball is
class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Block(Widget):
    pass

#instantiates a ball, defines it's motion
#places a block
class Game(Widget):
    playerBall = ObjectProperty(None)
    obstructionL = Widget()
    obstructionR = Widget()
    obstructionU = Widget()
    obstructionD = Widget()

    mouseVelocity = Vector(0.0, 0.0)
    mousePos = Vector(0.0,0.0)
    mousePrevPos = Vector(0.0,0.0)

    def update(self, dt):
        #update mouse velocity
        if dt != 0:
            #self.mouseVelocity = (self.mousePos - self.mousePrevPos)/dt
            self.mouseVelocity[1] = (self.mousePos[1] - self.mousePrevPos[1]) /(30*dt)
            self.mouseVelocity[0] = (self.mousePos[0] - self.mousePrevPos[0]) / (30*dt)
        #update mouse position
        self.mousePrevPos = self.mousePos


        #bounces off top/bottom
        if (self.playerBall.y < 0):
            self.playerBall.y = 0
            self.playerBall.velocity[1] *= -1
        if (self.playerBall.top > self.height):
            self.playerBall.top = self.height
            self.playerBall.velocity[1] *= -1

        #bounces off walls
        if (self.playerBall.x < 0):
            self.playerBall.x = 0
            self.playerBall.velocity[0] *= -1
        if (self.playerBall.right > self.width):
            self.playerBall.right = self.width
            self.playerBall.velocity[0] *= -1

        #bounces off Block
        if self.obstructionL.collide_widget(self.playerBall):
            self.playerBall.velocity[0] *= -1
        if self.obstructionR.collide_widget(self.playerBall):
            self.playerBall.velocity[0] *= -1
        if self.obstructionU.collide_widget(self.playerBall):
            self.playerBall.velocity[1] *= -1
        if self.obstructionD.collide_widget(self.playerBall):
            self.playerBall.velocity[1] *= -1

        self.playerBall.move()


    def on_touch_move(self, touch):
        #update mouse pos
        self.mousePos = touch.pos

        #check if touch collides with the ball
        if self.playerBall.collide_point(touch.x, touch.y) is True:

        #limit speed
            if self.mouseVelocity[0] > 10:
                self.mouseVelocity[0] = 10
            if self.mouseVelocity[0] < -10:
                self.mouseVelocity[0] = -10
            if self.mouseVelocity[1] > 10:
                self.mouseVelocity[1] = 10
            if self.mouseVelocity[1] < -10:
                self.mouseVelocity[1] = -10

        #set ball velocity
            self.playerBall.velocity = self.mouseVelocity




class BallMotionApp(App):
    def build (self):
        play = Game()
        Clock.schedule_interval(play.update, 1.0/60.0)
        return play



if __name__ == "__main__":
    BallMotionApp().run()
