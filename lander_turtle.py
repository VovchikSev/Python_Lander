import turtle, math, random

class Lander(turtle.Turtle):
    '''
    Purpose: Sets up Lander
    Instance variables:
        vx: the horizontal velocity
        vy: the vertical velocity
        fuel remaining: how much fuel is left in lander
    Methods:
        __init__: creates lander with inital attributes
        move: moves position of lander
        thrust: increases velocity by 1 in direction it is facing
        turn_left: turns lander left 10 degrees
        turn_right: turns lander right 10 degress
    '''
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        turtle.Turtle.__init__(self)
        self.penup()
        self.left(90)
        self.speed(0)
        self.setpos(x_pos, y_pos)
        self.vx = x_vel
        self.vy = y_vel
        self.fuel_remaining = 50
    def move(self):
        self.vy -= 0.0486
        # print(self.player.vy)
        x_pos = self.vx + self.xcor()
        y_pos = self.vy + self.ycor()
        # print(y_pos,x_pos)
        self.setpos(x_pos, y_pos)

    def thrust(self):
        if self.fuel_remaining > 0:
            print('Up button pressed')
            self.fuel_remaining -= 1
            facing = math.radians(self.heading())
            self.vx += math.cos(facing)
            self.vy += math.sin(facing)
            print(self.fuel_remaining)
        else:
            print('Out of fuel')

    def turn_left(self):
        if self.fuel_remaining > 0:
            print('Left arrow pressed')
            self.fuel_remaining -= 1
            self.left(10)
            print(self.fuel_remaining)
        else:
            print('Out of fuel')

    def turn_right(self):
        if self.fuel_remaining > 0:
            print('Left arrow pressed')
            self.fuel_remaining -= 1
            self.right(10)
            print(self.fuel_remaining)
        else:
            print('Out of fuel')


class Game():
    '''
    Purpose: sets up then runs the game
    Instance variables:
        player: lander creation
        meteor_list: list of meteors and attributes
    Methods:
        __init__: sets up work and lander with inputs
        gameloop: runs game and checks to see if win or loss conditions are met
    '''
    def __init__(self):
        turtle.setworldcoordinates(0,0,1000,1000)
        turtle.delay(0)

        self.player = Lander(random.uniform(100,900), random.uniform(500,900), random.uniform(-5,5), random.uniform(-5,5))
        self.player.turtlesize(1)
        self.meteor_list = []
        self.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.turn_left, 'Left')
        turtle.onkeypress(self.player.turn_right, 'Right')
        turtle.listen()
        turtle.mainloop()



    def gameloop(self):
        if self.player.ycor() < 10:
            if (self.player.vx < 3) and (self.player.vy > -3) and (self.player.vx > -3):
                # print(self.player.vx, self.player.vy)
                print('Successful landing!')
                return
            else:
                print('You crashed!')
                return
        for i in self.meteor_list:
            if i.crash_check(self.player.xcor(), self.player.ycor()) == True:
                print('You crashed!')
                return
        num1 = random.randint(1,21)
        if num1 == 1:
            new_meteor = Meteors(random.uniform(100,900), random.uniform(900,1000),random.uniform(-5,5), random.uniform(-15,0))
            self.meteor_list.append(new_meteor)

        self.player.move()
        for m in self.meteor_list:
            m.move_rock()
        turtle.Screen().ontimer(self.gameloop, 30)


class Meteors(turtle.Turtle):
    '''
    Purpose: to create and move meteors
    Instance variables:
        radius: radius of meteor
        y_vel: vertical velocity
        x_vel: horizontal velocity
    Methods:
        __init__: creates meteors
        move_rock: moves meteors with gravity
        crash_check: checks if lander has hit a meteor
    '''
    def __init__(self, pos_x, pos_y, xv, yv):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape('circle')
        self.radius = 20
        self.color('red')
        self.penup()
        self.setpos(pos_x, pos_y)
        self.y_vel = yv
        self.x_vel = xv
        self.showturtle()

    def move_rock(self):
        self.y_vel -= 0.0486
        pos_y = self.y_vel + self.ycor()
        pos_x = self.x_vel + self.xcor()
        self.setpos(pos_x, pos_y)

    def crash_check(self, x, y):
        if math.sqrt((x-self.xcor())**2 + (y-self.ycor())**2) < self.radius:
            return True
        else:
            return False

if __name__ == '__main__':
    Game()