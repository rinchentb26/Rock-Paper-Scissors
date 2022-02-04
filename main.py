import random
#ascii art for rock, paper and scissors
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
#inserting these strings onto a list
art=[rock,paper,scissors]

print("Let's Play Rock, Paper, Scissors!")
choice=int(input("What do you choose? Type 0 for Rock 🪨, 1 for Paper📰 2 for Scissors✂️\n"))
if choice<0 or choice>2:
    print("Invalid Input. You lose!")
else:
 print(art[choice])

 #generate random no b/w 0 and 2 for comp's choice
 ai=random.randint(0,2)
 print(f"Computer Chose {ai}")
 print(art[ai])

 # print results 
 if choice==ai:
  print("Arghh! It's a draw ¯\_( ° ⏥ ° )_/¯")
 elif choice==0 and ai==2:
  print("You win! ( ͡❛ ⏥ ͡❛)")
 elif choice==2 and ai==0:
  print("You lose! ¯\_( ᵔ ⏥ ᵔ )_/¯")
 elif choice>ai:
  print("You win! ( ͡❛ ⏥ ͡❛) ")
 else:
  print("You lose! ¯\_( ᵔ ⏥ ᵔ )_/¯")
