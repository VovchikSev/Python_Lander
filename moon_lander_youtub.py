
# по мотивам https://www.youtube.com/watch?v=DJxNUdsnsos 
# и git её https://github.com/MakingGamesByYear/Games/blob/master/Episode%200/lander_public.py
# более мнтересный проект, но требует разбора. https://github.com/epamekids/LunarLander/blob/master/README.md
class LanderGame:
    
    def __init__(self) :
        self.ballHeight = 1000 # метры
        self.running = True
        self.groundHeight =  0 # метры
        self.timeStep = 1.0  # секунды
        self.ballVelocity = 0.0 # meters per seond метры в секунду
        self.gravitationConstant = 9.8
        
        
        
    def updateTimeStep(self):
        aceleration = -self.gravitationConstant
        accelContribution = .5 * aceleration * self.timeStep * self.timeStep        
        
        self.ballHeight += self.ballVelocity * self.timeStep  + accelContribution       
        self.ballVelocity += aceleration * self.timeStep 
        
        print(f'Ball is at {self.ballHeight }')
        if self.ballHeight <= self.groundHeight:
            self.ballHeight = self.groundHeight
            print("The ball hits the floor with a thud")
            self.running = False
    def displayGameState(self):
        # вывести две стоки в первой подписи к данным, константа во второй данные из класса ..
        print(f'Time:{self.timeStep}(s) Height:{self.ballHeight}(m) Velocity: {self.ballVelocity}')
                
    def landerTotalMass(self):
        pass
    
    def handleInput(self):
        # skip input if we're out of fuel
        if self.landerFuel == 0:
            return
        message = '\n Enter your fuel burn rate (or type quit)'
        # inputstr = raw_input(message)
        while True:
            pass
            
            
    def getAcelerationFromThrust(self, fuelBurned):
        specificImpulse = 3050 # meter per second 
        # use the definition of specific impulse to get the force
        force = (fuelBurned / LanderGame.DeltaTimeSeconds) * specificImpulse
        # use f = ma to get the acceleration
        return force / self.landerTotalMass()
    
    
            
game = LanderGame()            

while game.running:
    # game.updateTimeStep()
    game.updateTimeStep()
    game.displayGameState()
        
# есть интересный пример https://github.com/mislitzer/lunar_lander/ на аркеде 18го года...
"""
Пример простого способа реализации        
# PLEASE CHANGE THE SPEED, FUEL, AND ALTITUDE VARIABLES TO YOUR LIKING
# you are the pilot and need to control how much fuel you burn in the
# retro rockets so that your descent speed slows to zero just as your
# altitude above the moon's surface reaches zero. If you impact the moon
# more than 5 m below the surface, or your speed on impact is
# greater than 5 m/s then you have considered to have crashed.
# else, it is considered to be a 'done' landing.
# If you run out of fuel, the spaceship will accelerate towards the moon by gravity.
# set up the initial parameters
speed = 20      # speed approaching the moon
fuel = 1500     # how much fuel is left
altitude = 100 # altitude above moon
gravity = 1 # acceleration due to gravity
burn = 0        # initial rate of burning fuel in rockets
# while ship is above the moon's surface,
# calculate flight data and take input from user
while altitude > 0:
   # calculate how long until ship will impact moon at current speed (impact)
   if speed <= 0:
       impact = 1000
   else:
       impact = altitude / speed
   # display flight data
   print('Altitude = ', altitude, 'Speed = ', speed, 'Fuel = ', fuel, 'Impact = ', impact, 'Previous burn', burn)
   burn = float(input("Enter fuel to burn (0-50)?"))
   # ensure rate of fuel burning is within rocket's capability and doesn't exceed remaining fuel
   if burn < 0:
       burn = 0
   if burn > 50:
       burn = 50
   if burn > fuel:
       burn = fuel
   #calculate new flight data
   altitude -= speed
   speed += gravity - burn/10
   fuel -= burn
# Hit moon surface
# display good landing or not
print('Altitude = ', altitude, 'Speed = ', speed, 'Fuel = ', fuel, 'Impact = ', impact, 'Previous burn', burn)
if altitude <- 5 or speed > 5:
   print("You have crashed")
else:
   print("You have landed")
        """