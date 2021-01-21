import random
import string

from ..model.password import Password

def generatePasswords(passType, length, amount):
  passwords = []

  if passType == "digit":
    for i in range(amount):
      passwords.append(Password(passType=passType, content="".join(random.choice(string.digits) for j in range(length))))
  elif passType == "lowercase":
    for i in range(amount):
      passwords.append(Password(passType=passType, content="".join(random.choice(string.ascii_lowercase) for j in range(length))))
  elif passType == "letter":
    for i in range(amount):
      passwords.append(Password(passType=passType, content="".join(random.choice(string.ascii_letters) for j in range(length))))
  elif passType == "letter_digit":
    for i in range(amount):
      passwords.append(Password(passType=passType, content="".join(random.choice(string.ascii_letters + string.digits) for j in range(length))))
  elif passType == "letter_digit_symbol":
    for i in range(amount):
      passwords.append(Password(passType=passType, content="".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for j in range(length))))
  else:
    return None

  return passwords