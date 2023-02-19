import random
import re
import sys


class GameGhost:
    def __init__(self):
        self.game_level = 1
        self.dors_ghosts = {}
        self.dors_count = 0
        self.user_dor_select = 0
        self.user_score = 0

    def game_instriction(self):
        hello_text = 'Та почнеться гра!'
        rule_text = 'Треба вгадати дверi за якими нема привида!'
        exit_text = 'для виходу введiть \'X\''
        print(hello_text.center(100, '-'))
        print(rule_text.center(100, '-'))
        print(exit_text.center(100, '_'))

    def rand_ghost_placement(self, level):
        for i in range(0, level):
            self.dors_ghosts[random.randint(0, len(self.dors_ghosts)-1)] = 'G'

    def set_level(self, add_level):
        self.game_level += add_level

    def add_point(self, point):
        self.user_score += point

    def set_dors_count(self, param):
        self.dors_count = param


    def create_dors(self):
        print('Введiть бажану кiлькысть дверей: мiн 5 мак 20')
        self.set_dors_count(self.check_input(input('Ваш вибiр: '), False))
        if 5 <= self.dors_count <= 20:
            for i in range(0, self.dors_count):
                self.dors_ghosts[i] = ''
        elif self.dors_count < 5 or self.dors_count > 20:
            for i in range(0, 5 if self.dors_count < 5 else 20):
                self.dors_ghosts[i] = ''


    def restart_game(self, flag):
        if flag:
            self.user_score = 0
            self.create_dors()
            for i in range(0, len(self.dors_ghosts)):
                self.dors_ghosts[i] = ''
            self.game_level = 1
        else:
            self.start_game()

    def check_input(self, param, flag):
        if flag:
            try:
                var = param
                if re.match("^[0123456789]*$", param):  # тiльки цифри
                    if int(var) <= len(self.dors_ghosts):
                        return int(var)
                else:
                    if var == 'x' or var == 'X':
                       sys.exit()
                    else:
                        raise Exception

            except:
                print('Введено некоректне значення')
                self.get_numbers()
        else:
            try:
                if re.match("^[0123456789]*$", param):  # тiльки цифри
                    return int(param)
                else:
                     if param == 'x' or param == 'X':
                        #sys.exit()
                        exit()
                     else:
                        raise Exception
            except:
                print('Введено некоректне значення')
                self.create_dors()

    def get_numbers(self):
        for i in range(0, len(self.dors_ghosts)):
            print(f'-[{i+1}]-', end='')
        self.user_dor_select = self.check_input(input('\nВаш вибiр: '), True)

    def print_result(self):
        var = '-'
        for i in range(0, len(self.dors_ghosts)):
            print(f'-[{i+1}]-', end='')
        print('\n')
        for i in range(0, len(self.dors_ghosts)):
            print(f'-[{self.dors_ghosts[i]}]--', end='')
        print('\n')

    def is_empty_door(self, dor_number):
        flag = False
        flag = True if self.dors_ghosts[dor_number-1] == '' else False
        return flag

    def is_new_game(self):
        flag = False
        if len(self.dors_ghosts) <= 0:
            return True
        else:
            return False

    def start_game(self):
        if self.is_new_game():
            self.create_dors()
        print_level = f'Поточний рiвень гри {self.game_level}'
        print(print_level.center(100, ' '))
        self.rand_ghost_placement(self.game_level)
        self.get_numbers()
        if self.is_empty_door(self.user_dor_select):
            self.add_point(10)
            self.set_level(1)
            print(f'Ви виграли! Ваш рахунок {self.user_score}')
            self.print_result()
            self.restart_game(False)
        else:
            print(f'Ви програли! Ваш рахунок {self.user_score}')
            self.print_result()
            print('Бажаете зiграти ще? Y/N: ')
            var = input()
            if var == 'y' or var == 'Y':
                self.restart_game(True)
                self.start_game()



game = GameGhost()
game.game_instriction()
game.start_game()

# rand_ghost_placement(3)
# print(dors_ghosts)