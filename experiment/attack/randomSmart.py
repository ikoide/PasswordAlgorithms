import random
import string

def randomSmartAttack(password):
  guesses = []
  if password.passType == "digit":
    while not password.cracked:
      guess = "".join(random.choice(string.digits) for i in range(password.getLength()))
      if not guess in guesses:
        guesses.append(guess)
        if password.content == guess:
          password.cracked = True
  elif password.passType == "lowercase":
    while not password.cracked:
      guess = "".join(random.choice(string.ascii_lowercase) for i in range(password.getLength()))
      if not guess in guesses:
        guesses.append(guess)
        if password.content == guess:
          password.cracked = True
  elif password.passType == "letter":
    while not password.cracked:
      guess = "".join(random.choice(string.ascii_letters) for i in range(password.getLength()))
      if not guess in guesses:
        guesses.append(guess)
        if password.content == guess:
          password.cracked = True
  elif password.passType == "letter_digit":
    while not password.cracked:
      guess = "".join(random.choice(string.ascii_letters + string.digits) for i in range(password.getLength()))
      if not guess in guesses:
        guesses.append(guess)
        if password.content == guess:
          password.cracked = True
  elif password.passType == "letter_digit_symbol":
    while not password.cracked:
      guess = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(password.getLength()))
      if not guess in guesses:
        guesses.append(guess)
        if password.content == guess:
          password.cracked = True