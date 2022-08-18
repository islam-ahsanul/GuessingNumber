import  random
secret_number=random.randint(1,20)
print("I am thinking of a number between 1 and 20.")

final_guess=0
final_try=0
left=5
for start in range(1,6):
    print("Guess that number.You have {} chances left.".format(left))
    guess=int(input())
    if(guess<secret_number):
        print('Your guess is too low.')
    elif(guess>secret_number):
        print('Your guess is too high.')
    else:
        final_guess=guess
        final_try=start
        break
    left -=1

if(final_guess==secret_number):
    print("Well done! You guessed my number in {} guesses.".format(final_try))
else:
    print("Failed! The number I was thinking of was {}.".format(secret_number))