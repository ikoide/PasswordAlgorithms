import time

from .util.color import Color

from .tools.generatePass import generatePasswords
from .attack.bruteForce import bruteForceAttack
from .attack._random import randomAttack
from .attack.randomSmart import randomSmartAttack
from .attack.dictionary import dictionaryAttack

passTypes = ["digit", "lowercase", "letter", "letter_digit", "letter_digit_symbol"]
methods = ["brute", "random", "randomSmart"]

def autoRun():
  with open("experiment/out/output.txt", "a") as f:
    f.truncate(0)
    f.write("Method, Type, Length, Avg Time\n")
  for i, j in enumerate(passTypes):
    for method in methods:
      for k in range(8):
        passwords = generatePasswords(j, k+1, 50)
        times = []
        for count, password in enumerate(passwords):
          startTime = time.time()
          if method == "brute":
            bruteForceAttack(password)
          elif method == "random":
            randomAttack(password)
          elif method == "randomSmart":
            randomSmartAttack(password)
          runTime = time.time() - startTime
          times.append(runTime)
          
        avgTime = sum(times)/len(passwords)
        with open("experiment/out/output.txt", "a") as f:
          f.write(f"{method}, {j}, {k+1}, {avgTime}\n")