import random

def game():
  player=input("Please choose a symbol from the given options--> ")
  computer = random.choice(['R','P','S'])
  print("Computer chose", computer)
  if player == computer:
    print("It's a tie match!")
  elif u_win(computer, player):
    print("You win!!")
  else:
    print("You lost")
  again()
  
def u_win(computer, player):
  if (player== 'R' and computer=="S") or (player== 'P' and computer=="R") or (player== 'S' and computer=="P"):
    return True
    
def again():
  print("Do you want to play again?")
  q=input("Select Y is Yes & N for No: ")
  if q=="Y":
    game()
  else:
    print("Exit")
  
print("Welcome to Rock, Paper and Scissors\nR is for Rock, P is for Paper and S is for Scissors")
game()
