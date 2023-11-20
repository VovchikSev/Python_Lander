from random import randint
# переработа lander_public.py для понимани работы процесса

# переработать на оптимальную работу по алгоритму, сделать нормально работающий класс игры, отдельно корабля. 
# корабль это объект класса игры.
#  особо разобраться с формулами выисления

# разного рода константы лучше вынести из класса

class ShipLanderGame(object):
    GravitationalConstant = 1.62 # Gravitational constant on the moon, in m/s
    DeltaTimeSeconds = 10.0      # time elapsed for each "frame" of the game

    LanderEmptyMass = 6834 #kilograms mass of lander without any fuel

    #Maximum velocity for perfect, good, and imperfect landings -- in meters/second
    # Максимальная скорость для идеальной, удачной и неудачной посадки - в метрах в секунду
    PerfectTouchdownVelocity = .536448
    GoodTouchdownVelocity = 4.4704 # скорость посадки при которой выжили
    ShipDamagedVelocity = 26.8224  # скорость посадки при которой корабль поврежден

    MinimumLanderFuelBurnRate = 1.50  #minimum KG/s fuel burn rate to produce acceleration
    MaximumLanderFuelBurnRate = 15  #maximum KG/s fuel burn rate    

    def __init__(self):
        self.running = True # посадка в процессе
        self.groundHeight = 0.0  # высота грунта, столкновение чревато
        self.missionTime = 0.0   # время миссии
        # можно выносить в отдельный класс Lander
        self.landerHeight = 15000.0 # начальная высота
        self.landerVelocity = 0.0 #-1700.0  ускорение, начинается с нуля?
        self.currentBurnRate = 0.0  # текущее ускорение в обратную сторону, торможение
        self.landerFuel = 8200 #kilograms, initial fuel, начальное количество топлива.

        self.gameIntro() # показать начальное интро



    def displayGameRate(self):
        print(f"Время посадки {self.missionTime}(s) Высота {self.landerHeight}(m) Ускорение {self.landerVelocity}(m/s) Топливо {self.landerFuel}(kg) Общая масса {self.landerTotalMass()}(kg)")
        

    def gameIntro(self) :
        # printFileContents("game_introfile.txt", ShipLanderGame.DefaultIntroStory)
        self.printInstructions()      

    def landerTotalMass(self):
        return ShipLanderGame.LanderEmptyMass + self.landerFuel


    def printInstructions(self): # переписать инструкцию.
        print(f'Инструкция \n' + '='*29 +'\nВы быстро запоминаете свои тренировки')
        print(f'У вас будет возможность регулировать тягу спускаемого аппарата каждыe {ShipLanderGame.DeltaTimeSeconds} секунд.')
        print (f'Вы регулируете работу двигателей, выбирая скорость сжигания топлива. Ноль - это свободное падение, или выберите скорость сжигания топлива от {ShipLanderGame.MinimumLanderFuelBurnRate} до {ShipLanderGame.MaximumLanderFuelBurnRate} кг/с')
        print(f'Масса вашего корабля без топлива составляет {ShipLanderGame.LanderEmptyMass} кг. В данный момент у вас есть {self.landerFuel} кг топлива. Для тех из вас, астронавтов, кто плохо разбирается в математике, это в общей сложности {self.landerTotalMass} кг. Разгонять посадочный модуль будет легче по мере того, как вы будете сжигать больше топлива')
        print(f'У вас идеальная безопасная скорость приземления в {ShipLanderGame.PerfectTouchdownVelocity} м/с')
        print('Удачи...')

    def run(self):
        while self.running == True :
            self.displayGameState()
            self.handleInput()

            if not self.running :
                continue
            
            self.updateTimeStep()

    def velocityToCraterDepthMeters(self, velocity): # вычисление глубины образовавшегося кратера...
        return -0.03093051878 * velocity # почему выбрана эта самая константа, непонятно и поиск ничего не дал, надо искать дальше.



def run_programm(): 
    # в оригинале какая то дичь, сделать что то по своему, чтобы как то работало.
    game = ShipLanderGame()
    game.run()


if __name__ == '__main__':
    run_programm()