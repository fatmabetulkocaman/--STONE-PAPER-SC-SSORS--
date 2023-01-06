print("""
------------------------
- STONE-PAPER-SCİSSORS -
Rules:
- Stone for "stone"
- Paper for "paper"
- Scissors for "scissors"
- Score = 3 -> win
------------------------

""")
import random
import time

your_score = 0
random_score = 0
def random_choice1():

    random_choice2 = random.randint(1,3)
    if random_choice2 == 1:
        return "stone"

    elif random_choice2 == 2:
        return "paper"

    elif random_choice2 == 3:
        return "scissors"


while True:
    your_choice = input("Make a choice:")
    random_choice = random_choice1()

    if random_choice == your_choice:
        time.sleep(2.1)
        print("Your choice:",your_choice and "Random choice:",random_choice)
        print("The choices are the same.Again,please..")

    elif random_choice == "stone" and your_choice == "paper":
        time.sleep(2.1)
        print("Your choice:",your_choice and "Random choice:",random_choice)
        your_score += 1

    elif random_choice == "paper" and your_choice == "scissors":
        time.sleep(2.1)
        print("Your choice:",your_choice and "Random choice:",random_choice)
        your_score += 1

    elif random_choice == "scissors" and your_choice == "stone":
        time.sleep(2.1)
        print("Your choice:",your_choice and "Random choice:",random_choice)
        your_score += 1

    else:
        time.sleep(2.1)
        print("Your choice:",your_choice and "Random choice:",random_choice)
        random_score += 1

    print("Your score: {} and Random score: {}".format(your_score,random_score))

    if random_score == 3 :
        break

    elif your_score == 3:
        break

if random_score > your_score:
    print("You lost!")

elif your_score > random_score:
    print("Congratulations, you won.")
else:
    print("You are tied.")