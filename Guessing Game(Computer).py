import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 & {x}: '))
        if guess<random_number:
            print("Sorry Try Again. Too Low.")
        elif guess>random_number:
            print("Sorry Try Again.Too High.")
    print(f"Yay you have guessed the number {random_number} correctly!!")
guess(100)