# This is a sample Python script.
import random

class gameMaster:
    gameField = []
    target = None
    middleFlag = None
    continueInterrogation = None

    def __init__(self, arrSize):
        self.arrStart = 0
        self.arrEnd = arrSize - 1
        gameMaster.gameField = [self.arrStart, self.arrEnd]
        gameMaster.target = random.randint(self.arrStart, self.arrEnd)
        gameMaster.middleFlag = (gameMaster.gameField[0] + gameMaster.gameField[1]) // 2
        gameMaster.continueInterrogation = True
        print(f'[{gameMaster.target}]\n')

    def interrogation(self):

        while gameMaster.continueInterrogation == True:
            print(f'interrogating officier: ')
            print(f'{gameMaster.gameField[0]}_{gameMaster.middleFlag}_{gameMaster.gameField[1]}')

            self.interrStage_0()
            self.interrStage_1()


    def interrStage_0(self):
        if gameMaster.target == gameMaster.gameField[0]:
            self.result(gameMaster.gameField[0])
        elif gameMaster.target == gameMaster.middleFlag:
            self.result(gameMaster.middleFlag)
        elif gameMaster.target == gameMaster.gameField[1]:
            self.result(gameMaster.gameField[1])

    def interrStage_1(self):

        if gameMaster.target > gameMaster.gameField[0] and \
                gameMaster.target < gameMaster.middleFlag:
            gameMaster.gameField[1] = gameMaster.middleFlag

        elif gameMaster.target > gameMaster.middleFlag and \
                gameMaster.target < gameMaster.gameField[1]:
            gameMaster.gameField[0] = gameMaster.middleFlag

        gameMaster.middleFlag = (gameMaster.gameField[0] + gameMaster.gameField[1]) // 2


    def result(self, target):
        print(f'\nthe value of target is {gameMaster.target}')
        gameMaster.continueInterrogation = False

def main():
    goParse = True
    fieldSize = None

    while goParse == True:
        fieldSize = input("give the size of field for game >> ")
        try:
            fieldSize = int(fieldSize)
        except ValueError:
            print(f'incorrect value... {fieldSize}')
        else:
            if fieldSize > 0:
                goParse = False
            else:
                print(f'incorrect value... {fieldSize}')

    print(f'size of field for game is {fieldSize}\n')
    gm = gameMaster(fieldSize)
    gm.interrogation()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


