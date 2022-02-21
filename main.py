import random
# ascii art for rock, paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# inserting these strings onto a list
art = [rock, paper, scissors]

print("Let's Play Rock, Paper, Scissors! First to score 3 points wins.")
name = input("What's your name? ")
player_score = 0
comp_score = 0
runProgram = True
print("Let's play!")
while(runProgram):
    choice = int(
        input("What do you choose? Type 0 for Rock 🪨, 1 for Paper📰 2 for Scissors✂️\n"))
    if choice < 0 or choice > 2:
        print("Invalid Input. You lose!")
    else:
        print(art[choice])

    # generate random no b/w 0 and 2 for comp's choice
    ai = random.randint(0, 2)
    print(f"Computer Chose")
    print(art[ai])

    # print results
    if choice == ai:
        print("Arghh! It's a draw ¯\_( ° ⏥ ° )_/¯")
    elif choice == 0 and ai == 2:
        print("You win! ( ͡❛ ⏥ ͡❛)")
        player_score += 1
    elif choice == 2 and ai == 0:
        print("You lose! ¯\_( ᵔ ⏥ ᵔ )_/¯")
        comp_score += 1
    elif choice > ai:
        print("You win! ( ͡❛ ⏥ ͡❛) ")
        player_score += 1
    else:
        print("You lose! ¯\_( ᵔ ⏥ ᵔ )_/¯")
        comp_score += 1
    if player_score == 3 or comp_score == 3:
        print("\n**🏁 Final Score ** 🏁")
        print(f"Computer - {comp_score} {name} - {player_score}")
        break
    print("**🏁 Current Score ** 🏁")
    print(f"   Computer - {comp_score} {name} - {player_score}  ")
