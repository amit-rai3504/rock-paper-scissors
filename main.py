import random
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

choices = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(user_choice)
user_choice = choices[user_choice]
print(user_choice)
computer_choice = random.choice(choices)

while(user_choice == computer_choice):
    computer_choice = random.choice(choices)


print("Computer choices:")
print(computer_choice)

if user_choice == rock and computer_choice == scissors:
  print("Congrats you Won!!")
elif user_choice == scissors and computer_choice == paper:
  print("Congrats you Won!!")
elif user_choice == paper and computer_choice == rock:
  print("Congrats you Won!!")
else:
  print("Better luck next time")
