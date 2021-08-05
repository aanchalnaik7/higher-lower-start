import random
from art import logo, vs
from game_data import data

def format_data(account):
  """takes the account data and returns the printable format"""
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"

def check(guess, a_followers, b_followers):
  """Takes the user guess and follower counts of a and b and returns if they got it right"""
  if a_followers > b_followers:
    """if guess == "a":
      return True
    else:
      return False"""
    return guess == "a"
  else:
    return guess == "b"


# display art
print(logo)
score = 0
game_should_continue = True
# generat a random account from the game data
account_b = random.choice(data)

# making the game repeatable
while game_should_continue:

  # making account at position b become the next account at position a
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  # ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B'\n").lower()

  # check if user is correct 
  ## get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check(guess, a_follower_count, b_follower_count)

  print(logo)

  # give user feedback on their guess
  # score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score is {score}.")
  else:
    game_should_continue = False
    print(f"Sorry that is wrong! Final score is {score}.")
 