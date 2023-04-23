print("The player is a hacker who has to infiltrate a secret facility and stop an evil AI")
print("The game is text-based.")
# A sci-fi novel game

import random
name = input("Enter your name: ") # The player's name
password = random.randint(0, 999999) # The password to access the facility
inventory = [] # The items the player has
health = 100 # The player's health
ai_health = 100 # The AI's health

# Define some functions
def hack():
  # A function to hack a terminal and get information or items
  global password
  global inventory
  global health
  print("You approach a terminal. It asks for a password.")
  guess = input("Enter password: ")
  if guess == password:
    print("Access granted.")
    print("You find some useful information or items.")
    inventory.append("data")
    print("Your inventory:", inventory)
  else:
    print("Access denied.")
    print("An alarm goes off. You lose some health.")
    health -= 5
    print("Your health:", health)

def fight():
  global health
  global ai_health
  if ai_health <=0:
    print("No emeny")
  else:
    print("You encounter an enemy. It attacks you.")
    action = input("Do you want to fight back(Y) or run away(N) ?")
    if action == "Y":
     print("You fight back.")
     print("You deal some damage to the enemy.")
     ai_health -= 20
     print("The AI's health:", ai_health)
     print("The enemy deals some damage to you.")
     health -= 10
     print("Your health:", health)
    elif action == "N":
     print("You run away.")
     print("You escape the enemy but lose some time.")
    else:
     print("Invalid action. You lose some health.")
     health -= 10
     print("Your health:", health)

def end():
  # A function to end the game
  global health
  global ai_health
  if health <= 0:
    print("You have no health left. You die.")
    print("Game over. You lose.")
  elif ai_health <= 0:
    print("The AI has no health left. You destroy it.")
    print("Game over. You win.")
  else:
    print("The AI activates its doomsday device.")
    print("Game over. You lose.")

# Start the game
print(f"Welcome to the sci-fi novel game, {name}.")
print("You are a hacker who has to infiltrate a secret facility and stop an evil AI.")
print("You have limited time and health. Be careful.")

# Main loop
while True:
  if health <= 0:
    end()
  elif ai_health <= 0:
    end()
  else:
   print("\nWhat do you want to do?")
   print("1. Hack a terminal")
   print("2. Fight an enemy")
   print("3. End the game")

  # Get the choice
  choice = input("Enter your choice: ")

  # Execute the choice
  if choice == "1":
    hack()
  elif choice == "2":
    fight()
  elif choice == "3":
    end()
    break # Exit the loop
  else:
    print("Invalid choice. Try again.")