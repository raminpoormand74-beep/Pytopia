import random

def validate_guess(user_guess):
    if not user_guess.isdigit():
        print('Invalid input. please try again')
        return False
    user_guess = int(user_guess)

    if not 1 <= user_guess <= 100:
        print('Your guess is out of range. Please try again. Choose between 1 to 100')
        return False

    return True

def main():
    while True:
        rand_num = random.randint(1, 100)
        score = 100

        while True:
            user_guess = input('Guess a number between 1 to 100: ')

            if user_guess.lower() == 'q':
                print('Goodbye')
                return
                

            if not validate_guess(user_guess):
                continue

            user_guess = int(user_guess)

            if user_guess > rand_num:
                print('Your guess is too high')
            elif user_guess < rand_num:
                print('Your guess is too low')
            else :
                print('Congratulations! You guessed the correct number!')
                print(f'Your score is: {score}')
                wanna_play_again = input('Do you wanna play again ? y/n ')
                if wanna_play_again == 'y':
                    break
                elif wanna_play_again == 'n':
                    print('Goodbye')
                    return
                else:
                    print('Enter y/n ')
            score -= 5
            score = max(score, 0)

if __name__ == '__main__':
    main()

