
from os import system
from random import randint

def clear_scr():
    """ clears screen """
    try:
        system("cls")
    except:
        system("clear")

def round_up_num(num):
    """ rounds up the float/decimal number. """
    if num - int(num) > 0.5:
        return int(num)+1
    
    else:
        return int(num)


class HangManWord:

    def __init__(self) -> None:
        self.word = ''
        self.word_len = len(self.word)
        self.dash = ['_' for _ in range(self.word_len)]     ## stores '_' times length of word
        self.guessed_letter = set()

    def get_word(self, word):
        """ updates new word to start new game """
        self.word = word
        self.word_len = len(self.word)
        self.dash = ['_' for _ in range(self.word_len)]
        self.guessed_letter = set()

    def get_indexs(self, guessed_letter):
        inds = []
        if guessed_letter in self.word:
            for ind, letter in enumerate(self.word):
                if guessed_letter == letter:
                    inds.append(ind)

        return inds

    def give_hints(self):
        """ give hints to the player who is guessing. like if word is 'python' hint will be '_ y _ h _ n """

        no_of_hints_to_give = round_up_num(self.word_len*(30/100))
        for _ in range(no_of_hints_to_give):
            random_ind = randint(0, self.word_len-1)
            self.dash[random_ind] = self.word[random_ind]

    def play(self, hint=True):
        """ starts the game. If hint is true hint will be given to guesser. """

        attempts = 6
        if hint:
            self.give_hints()

        while attempts > 0:
            clear_scr()
            print(f"You got: {attempts} attempt left")
            print(' '.join(self.dash))

            if self.word == ''.join(self.dash):
                return True

            letter = input("Guess a letter: ")

            if letter in self.guessed_letter:
                continue

            if letter in self.word:
                inds = self.get_indexs(letter)
                for i in inds:
                    self.dash[i] = letter
            else:
                attempts -= 1

            self.guessed_letter.add(letter)
        
        return False



if __name__ == "__main__":
    game = HangManWord()

    word = input("Choose a Word: ")
    game.get_word(word)
    run = True
    while run:


        status = game.play(hint=True)
        if status:
            print("You won!")
        else:
            print(f"The word was {word.upper()}")
            print("You loose!")

        choose = input("Start again?[y/(any)]: ")
        if choose == 'y':
            word = input("Word: ")
            game.get_word(word)
        else:
            run = False
