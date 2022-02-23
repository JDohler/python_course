from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            ## total += 1 is it wrong once doenst matter what value you guess, the result always was 5. 
            total += die.value 
        return total

    @classmethod
    def run(cls):
        c = 0
        runner = cls() 
        
        while True:
          ## runner = cls() is not right should called outside of while, otherwise the counting wont change
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again? Type y or press enter to play again or type n to ended the game]: ") ## [Y/n] with capital letter is not right. We should change for y

            if prompt == 'y' or prompt == '':
                continue 
            elif prompt == 'n': ## missing this part
                print('Ended game')
                break
            else:
                i_just_throw_an_exception()
               