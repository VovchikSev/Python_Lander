GravitationalConstant = 1.62  # Gravitational constant on the moon, in m/s


class Lander(object):
    empty_mass = 6834  # масса спускаемого аппарата в килограммах без какого-либо топлива
    min_fuel_burn_rate = 1.5
    max_fuel_burn_rate = min_fuel_burn_rate * 10
    perfect_touchdown_velocity = .536448
    good_touchdown_velocity = 4.4704
    damaged_velocity = 26.8224

    def __init__(self, fuel: float = None, ):
        # килограммы, начальное количество топлива, поменять на случайное значение в диапазоне (10 000 - 8000)
        self.__fuel = 8200
        # начальная высота, сделать случайной величиной 3000 - 1500 примерный диапазон
        self.__height = 1500
        # затраченное количество топлива на предыдущем ходу.
        self.__current_burn_rate = 0.0
        self.__velocity = 0.0  # скорость

    @property
    def fuel(self):
        return self.__fuel

    @property
    def current_burn_rate(self):
        return self.__current_burn_rate

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    @property
    def total_mass(self):
        return self.empty_mass + self.__fuel
    
    def set_burn_rate(self, burn_rate):
        self.__fuel -= burn_rate # нужно вычислть затраченное толиво на шаг времени в секундах


class Game(object):
    # Время, затраченное на каждый "ход" игры. Или вовсе вынести в константы в отдельный файл
    DeltaTimeSeconds = 10.0

    @classmethod
    def game_intro(cls):
        pass

    def __init__(self):
        self.running = True
        self.mission_time = 0.0  # время миссии
        self.ground_height = 0.0  # уровень земли
        self.lander = Lander()

    def handle_input(self):
        # пропустить ввод если закончилось топливо
        if self.lander.fuel == 0:
            return
        information_message = 'Введите скорость сжигания топлива (или введите "Quit/q для выхода")'
        in_str = input(information_message)
        while True:
            if in_str.lower() in ['q', 'quit']:
                self.running = False
                return
            try:
                f_accel = float(in_str)
                if f_accel >= 0.0:
                    pass
                else:
                    pass
            except:
                print('Пожалуйста, введите число или введите quit!')
            in_str = input(information_message)

    def display_state(self):
        print(
            f"Время посадки {self.mission_time}(s) Высота {self.lander.height}(m) Ускорение {self.lander.velocity}"
            f"(m/s) Топливо {self.lander.fuel}(kg) Общая масса {self.lander.total_mass}(kg)")

    def print_instruction(self):
        # просто напечатать инструкцию при начальном запуске
        print(f'Инструкция \n' + '=' * 29 +
              '\nВы быстро запоминаете свои тренировки')
        print(
            f'У вас будет возможность регулировать тягу спускаемого аппарата каждый {self.DeltaTimeSeconds} секунд.')
        print(
            f'Вы регулируете работу двигателей, выбирая скорость сжигания топлива. Ноль - это свободное падение, '
            f'или выберите скорость сжигания топлива от {self.lander.min_fuel_burn_rate} до '
            f'{self.lander.max_fuel_burn_rate} кг/с')
        print(
            f'Масса вашего корабля без топлива составляет {self.lander.empty_mass} кг. ')
        print(f'В данный момент у вас есть {self.lander.fuel} кг топлива. Для тех из вас, астронавтов, кто плохо '
              f'разбирается в математике, это в общей сложности {self.lander.total_mass} кг. Разгонять посадочный '
              f'модуль будет легче по мере того, как вы будете сжигать больше топлива')
        print(
            f'У вас идеальная безопасная скорость приземления в {self.lander.perfect_touchdown_velocity} м/с')
        print('Удачи...')

    def update_time_step(self):
        pass

    def run(self):
        while self.running:
            self.display_state()
            if self.lander.fuel > 0:
                pass
            else:
                print('Топливо закончилось, мы падаем...')
            self.update_time_step()


def main():
    game = Game()
    while game.running:
        pass


if __name__ == '__main__':
    main()
