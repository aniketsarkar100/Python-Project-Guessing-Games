# import random
# def guess(x):
#     random_number=random.randint(1,x)
#     guess=0
#     while guess!=random_number:
#         guess=int(input(f'Guess a number between 1 & {x}: '))
#         if guess<random_number:
#             print("Sorry Try Again. Too Low.")
#         elif guess>random_number:
#             print("Sorry Try Again.Too High.")
#     print(f"Yay you have guessed the number {random_number} correctly!!")
# guess(10)
import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} Too High(H), Too Low(L) or Correct(C): ').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=="l":
            low=guess+1
    print(f'Yay! the computer guessed the number {guess} correctly')
computer_guess(1000)