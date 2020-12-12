import string as st
import random
import itertools as it
import time
import re

class Environment(object):
  def __init__(self):
    self.digits = st.digits
    self.lowercase = st.ascii_lowercase
    self.uppercase = st.ascii_uppercase
    self.letters = st.ascii_letters
    self.punctuation = st.punctuation
    
    self.data = {}
    
  def genDig(self, length): # All digits
    return ''.join(random.choice(self.digits) for i in range(length))

  def genLow(self, length): # All lowercase letters
    return ''.join(random.choice(self.lowercase) for i in range(length))

  def genStr(self, length): # All lowercase and uppercase letters
    return ''.join(random.choice(self.letters) for i in range(length))

  def genStrDig(self, length): # All letters and digits
    return ''.join(random.choice(self.letters + self.digits) for i in range(length))

  def genStrDigSym(self, length): # Letters, digits and symbols
    return ''.join(random.choice(self.letters + self.digits + self.punctuation) for i in range(length))

  def bruteForceAttack(self, password):
    if password.passType == "dig":
      for i in it.product(self.digits, repeat=len(password.content)):
        if password.content == ''.join(i):
          password.cracked = True
    if password.passType == "low":
      for i in it.product(self.lowercase, repeat=len(password.content)):
        if password.content == ''.join(i):
          password.cracked = True
    if password.passType == "str":
      for i in it.product(self.letters, repeat=len(password.content)):
        if password.content == ''.join(i):
          password.cracked = True
    if password.passType == "strDig":
      for i in it.product(self.letters + self.digits, repeat=len(password.content)):
        if password.content == ''.join(i):
          password.cracked = True
    if password.passType == "strDigSym":
      for i in it.product(self.letters + self.digits + self.punctuation, repeat=len(password.content)):
        if password.content == ''.join(i):
          password.cracked = True
          
  def randomAttack(self, password):
    cracked = False
    if password.passType == "dig":
      while not cracked:
        guess = self.genDig(len(password.content))
        if guess == password.content:
          cracked = True
          password.cracked = True
    if password.passType == "low":
      while not cracked:
        guess = self.genLow(len(password.content))
        if guess == password.content:
          cracked = True
          password.cracked = True
    if password.passType == "str":
      while not cracked:
        guess = self.genStr(len(password.content))
        if guess == password.content:
          cracked = True
          password.cracked = True
    if password.passType == "strDig":
      while not cracked:
        guess = self.genStrDig(len(password.content))
        if guess == password.content:
          cracked = True
          password.cracked = True
    if password.passType == "strDigSym":
      while not cracked:
        guess = self.genStrDigSym(len(password.content))
        if guess == password.content:
          cracked = True
          password.cracked = True
      
  def randomSmartAttack(self, password):
    guesses = []
    cracked = False
    if password.passType == "dig":
      while not cracked:
        guess = self.genDig(len(password.content))
        if guess not in guesses:
          if guess == password.content:
            cracked = True
            password.cracked = True
          guesses.append(guess)
    if password.passType == "low":
      while not cracked:
        guess = self.genLow(len(password.content))
        if guess not in guesses:
          if guess == password.content:
            cracked = True
            password.cracked = True
          guesses.append(guess)
    if password.passType == "str":
      while not cracked:
        guess = self.genStr(len(password.content))
        if guess not in guesses:
          if guess == password.content:
            cracked = True
            password.cracked = True
          guesses.append(guess)
    if password.passType == "strDig":
      while not cracked:
        guess = self.genStrDig(len(password.content))
        if guess not in guesses:
          if guess == password.content:
            cracked = True
            password.cracked = True
          guesses.append(guess)
    if password.passType == "strDigSym":
      while not cracked:
        guess = self.genStrDigSym(len(password.content))
        if guess not in guesses:
          if guess == password.content:
            cracked = True
            password.cracked = True
          guesses.append(guess)
          
  def dictionaryAttack(self, password):
    with open("rockyou.txt", "r", encoding="ISO-8859-1") as f:
      data = f.read().splitlines()
      for line in data:
        if line == password.content:
          password.cracked = True  
        
  def plot(self):
    pass      
          
  def run(self, algoType, passType, length, iterations):      
    passwords = []
    for i in range(iterations):
      if passType == "dig":
        password = Password(content=self.genDig(length), passType="dig")
        passwords.append(password)
      elif passType == "low":
        password = Password(content=self.genLow(length), passType="low")
        passwords.append(password)
      elif passType == "str":
        password = Password(content=self.genStr(length), passType="str")
        passwords.append(password)
      elif passType == "strDig":
        password = Password(content=self.genStrDig(length), passType="strDig")
        passwords.append(password)
      elif passType == "strDigSym":
        password = Password(content=self.genStrDigSym(length), passType="strDigSym")
        passwords.append(password)

    for i in passwords:
      startTime = time.time()
      if algoType == "bruteForce":
        self.bruteForceAttack(i)
      if algoType == "random":
        self.randomAttack(i)
      if algoType == "randomSmart":
        self.randomSmartAttack(i)
      if algoType == "dictionary":
        self.dictionaryAttack(i)
                
      i.crackTime = time.time() - startTime
    
    # Display results
    avgCrackTime = 0.0
    notCrackedCount = 0
    for i in passwords:
      if i.cracked:
        avgCrackTime += i.crackTime
      else:
        notCrackedCount += 1
        
    avgCrackTime /= len(passwords)
    
    print(f"Type: {passwords[0].passType}")
    print(f"Algo Type: {algoType}")
    print(f"Iterations: {str(len(passwords))}")
    print(f"Avg. Crack Time: {str(avgCrackTime)}")
    print(f"Not Cracked Count: {str(notCrackedCount)}")
        
class Password(Environment):
  def __init__(self, content, passType):
    super().__init__()
    self.content = content
    
    # Digits: dig
    # Lowercase Letters: low
    # All Letters: str
    # Letters and Digits: strDig
    # Letters, Digits and Symbols: strDigSym
    self.passType = passType
    
    self.cracked = False
    self.crackTime = 0.0
    

# from environment import Environment

if __name__ == "__main__":
  environment = Environment()
  environment.run(algoType="bruteForce", passType="low", length=4, iterations=4)