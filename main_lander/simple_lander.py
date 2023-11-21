
class LanderGame():
    def __init__(self):        
        self.speed = 20 # скорость приближения к Луне
        self.fuel = 1500  # сколько осталось топлива      
        self.altitude = 100 # высота над луной
        self.gravity = 1 # ускорение под действием силы тяжести
        self.burn = 0    # начальная скорость сжигания топлива в ракетах
        self.impact = 1000

    def show_flight_data(self):
        print(f'Высота: {self.altitude} Скорость: {self.speed} Топливо: {self.fuel} Влияние: {self.impact} Предыдущий газ: {self.burn}')


    def time_step(self):
        while self.altitude > 0:
            if self.speed <= 0:
                self.impact = 1000
            else:
                self.impact = self.altitude / self.speed
            # показать данные полета
            self.show_flight_data()
            self.burn = float(input('Ускорение (0 - 50): '))
            if self.burn < 0:
                self.burn = 0
            if self.burn > 50:
                self.burn = 50
            if self.burn > self.fuel:
                self.burn = self.fuel
            # вычислить новые данные полета
            self.altitude -= self.speed
            self.speed += self.gravity - self.burn / 10
            self.fuel -= self.burn
        # столкновение с поверхностью...
        # показать удачная посадка или нет.
        self.show_flight_data()        
        if self.altitude < -5 or self.speed > 5:
            print("Корабль разбился об поверхность")
        else:
            print('Удачная посадка')
def main():
    game = LanderGame() 
    game.time_step()


if __name__ == '__main__':
    main()