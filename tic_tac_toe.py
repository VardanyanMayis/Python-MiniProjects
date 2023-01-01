# Tic Tac Toe
# Program where person and computer can play Tic tac toe  together


import random


class TicTacToe:

    def __init__(self, person):
        self.Bord = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.winner = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                        [1, 4, 7], [2, 5, 8], [3, 6, 9],
                            [1, 5, 9], [7, 5, 3]]

        self.Empty = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.conmputerB = []
        self.personB = []
        self.who_winner = False

        if person in ('X', 'x'):
            self.personC = 'X'
            self.conmputerC = 'Y'
        else:
            self.conmputerC = 'X'
            self.personC = 'Y'

    def print_bord(self):
        print(f'{self.Bord[0]} | {self.Bord[1]} | {self.Bord[2]}')
        print('---------')
        print(f'{self.Bord[3]} | {self.Bord[4]} | {self.Bord[5]}')
        print('---------')
        print(f'{self.Bord[6]} | {self.Bord[7]} | {self.Bord[8]}')
        print('\n\n')

    def get_box_person(self):
        box = int(input('Choose a box: '))
        while not box in self.Empty:
            box = int(input(('Wrong box, Choose a new box:')))

        self.personB.append(box)
        self.Bord[box-1] = self.personC
        self.Empty.remove(box)

        for win_boxess in self.winner:
            win_boxes = win_boxess[:]
            for box in self.personB:
                if win_boxes.count(box) == 1:
                    win_boxes.remove(box)
            if len(win_boxes) == 0:
                return self.results('P')
        
        if len(self.Empty) == 0:
            return self.results('D')
        
        return self.results(None)
    
    def get_box_conmputer(self):
        # Attac
        for win_boxess in self.winner:
            win_boxes = win_boxess[:]
            if self.Bord[win_boxess[0]-1] and self.Bord[win_boxess[1]-1] and self.Bord[win_boxess[2]-1] != self.personC:
                for box in self.conmputerB:
                    if win_boxes.count(box) == 1:
                        win_boxes.remove(box)
                if len(win_boxes) == 1 and win_boxes[0] in self.Empty:
                    win_box = win_boxes[0]

                    self.conmputerB.append(win_box)
                    self.Bord[win_box-1] = self.conmputerC
                    self.Empty.remove(win_box)

                    return self.results('C')
        
        # Def 
        for win_boxess in self.winner:
            win_boxes = win_boxess[:]
            for box in self.personB:
                if win_boxes.count(box) == 1:
                    win_boxes.remove(box)
            if len(win_boxes) == 1 and win_boxes[0] in self.Empty:
                def_box = win_boxes[0]
                self.conmputerB.append(def_box)
                self.Bord[def_box-1] = self.conmputerC
                self.Empty.remove(def_box)
                return self.results(None)

        # another box
        if len(self.Empty) == 0:
            return self.results('D')

        box = random.choice(self.Empty)
        self.conmputerB.append(box)
        self.Bord[box-1] = self.conmputerC
        self.Empty.remove(box)

        return self.results(None)

    def results(self, who):
        if who == 'P':
            print('End game, You are winner!')
            self.who_winner = True
        elif who == 'D':
            print('Eng game, Draw!!')
            self.who_winner = True
        elif who == 'C':
            print('You are lose :)')
            self.who_winner = True


        return self.print_bord()


def main():
    color = ''
    while not color in ('X', 'Y'):
        color = input('X or Y: ')
    raund = TicTacToe(color)
    raund.print_bord()

    if color == 'X':
        while len(raund.Empty) != 0 and raund.who_winner == False:
            raund.get_box_person()
            if raund.who_winner == False:
                raund.get_box_conmputer()
            else:
                break
    else:
        while len(raund.Empty) != 0 and raund.who_winner == False:
            raund.get_box_conmputer()
            if raund.who_winner == False:
                raund.get_box_person()
            else:
                break
    print('End game')
    input('')


main()
