import os
import sys
import time

from .config import Configuration
from .util.color import Color
from .tools.generatePass import generatePasswords
from .attack.bruteForce import bruteForceAttack
from .attack._random import randomAttack
from .attack.randomSmart import randomSmartAttack
from .attack.dictionary import dictionaryAttack

class Experiment():
  def __init__(self):
    self.running = True
    self.print_banner()

    self.passwords = []

  def print_banner(self):
    Color.p("\n               __")
    Color.p("    ..=====.. |{R}=={W}|")   
    Color.p("    ||     || |{B}={W} |     {G}PasswordAlgorithms {D}v%s{W}" % Configuration.version)
    Color.p(" _  ||     || |{R}^{G}*{W}| _   {R}Created: {D}%s{W}" % Configuration.created_on)
    Color.p("|{G}={W}| o=,===,=o |__||{G}={W}|  {B}Author: {D}%s{W}" % Configuration.author)
    Color.p("|_|  _______)~`)  |_|") 
    Color.p("    [=======]  ()\n")   
      
  def commands(self, cmd):
    if cmd == "quit":
      self.running = False
      sys.exit()
    if cmd == "generate":
      passType = input("Password Type (digit, lowercase, letter, letter_digit, letter_digit_symbol): ")
      length = input("Length: ")
      amount = input("Amount: ")
      passwords = generatePasswords(passType, int(length), int(amount))
      if passwords:
        self.passwords = passwords
        Color.p("[+] Passwords set.")
      else:
        Color.p("[?] Password generation failed.")

    if cmd == "attack":
      attackType = input("Attack Type (brute, dictionary, random, randomSmart): ")
      Color.p(f"[*] [0/{len(self.passwords)}]")
      # Do not make verbose because terminal I/O slows down speed
      times = []
      for count, password in enumerate(self.passwords):
        startTime = time.time()
        if attackType == "brute":
          bruteForceAttack(password)
        elif attackType == "dictionary":
          dictionaryAttack(password)
        elif attackType == "random":
          randomAttack(password)
        elif attackType == "randomSmart":
          randomSmartAttack(password)
        runTime = time.time() - startTime
        times.append(runTime)
        password.time = runTime
        Color.p(f"[+] [{count+1}/{len(self.passwords)}]: Time: {runTime}")
      Color.p("[!] Done!")
      Color.p(f"[*] Average Time: {sum(times)/len(self.passwords)}")
    
    if cmd == "autorun":
      pass

  def start(self):
    while self.running:
      userIp = input("-[ ")
      self.commands(cmd=userIp)

def entry_point():
  try:
    exp = Experiment()
    exp.start()
  except Exception as e:
    Color.p('\n[!] Interuptted, Shutting down...')
    Color.p('[!] %s' % e)
    if e == ConnectionError:
      Color.p('[!] Could be due to SMTP protocol timing out.')