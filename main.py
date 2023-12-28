import random
def get_user_choice():
   choice = input("Enter your choice rock, paper,scissors ")

   while choice!='rock' and choice !="paper" and choice!="scissors":
       choice = input("Enter valid choice rock, paper,scissors ")

   print("Your choice",choice)
   return choice



def get_computer_choice():
     computerChoice = random.choice(["rock" ,"paper","scissors"])
     print("Computer Choice",computerChoice )
     return  computerChoice





def determine_winner(user_choice, computer_choice):

    if user_choice == "rock" and computer_choice=="scissors" :
        print("You Win!")
        return "user"

    elif user_choice=="rock" and computer_choice=="paper":
        print("Computer Wins!")
        return "computer"
    elif user_choice == "scissors" and computer_choice=="rock" :
        print("Computer Wins!")
        return "computer"

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Win!")
        return "user"

    elif user_choice == "paper" and computer_choice == "scissors":
        print("Computer Wins!")
        return "computer"

    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
        return "user"
    else:
        print("It's a tie!")


def rock_paper_scissors():
    cWin = 0
    uWin = 0
    while True:
      winner =  determine_winner(get_user_choice() ,get_computer_choice())
      if winner == "user":
          uWin +=1
      elif winner=="computer":
          cWin +=1
      anotherRound = input("Do You Want To Play Another Round ? yes or no ")
      if anotherRound == "no":
          print("user wins",uWin)
          print("computer wins",cWin)
          print("Program ends. Goodbye!")
          break



rock_paper_scissors()
input("press enter to exit") # i added this since when i run it using the cmd it closes wihout printing the result
