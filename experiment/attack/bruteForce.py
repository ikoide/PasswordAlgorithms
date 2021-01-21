import itertools
import string

def bruteForceAttack(password):
  if password.passType == "digit":
    for i in itertools.product(string.digits, repeat=password.getLength()):
      if password.content == "".join(i):
        password.cracked = True
  elif password.passType == "lowercase":
    for i in itertools.product(string.ascii_lowercase, repeat=password.getLength()):
      if password.content == "".join(i):
        password.cracked = True
  elif password.passType == "letter":
    for i in itertools.product(string.ascii_letters, repeat=password.getLength()):
      if password.content == "".join(i):
        password.cracked = True
  elif password.passType == "letter_digit":
    for i in itertools.product(string.ascii_letters + string.digits, repeat=password.getLength()):
      if password.content == "".join(i):
        password.cracked = True
        return True
  elif password.passType == "letter_digit_symbol":
    for i in itertools.product(string.ascii_letters + string.digits + string.punctuation, repeat=password.getLength()):
      if password.content == "".join(i):
        password.cracked = True