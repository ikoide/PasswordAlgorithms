import os
import sys

from .config import Configuration
from .util.color import Color

class Experiment():
  def __init__(self):
    self.running = True
    self.print_banner()

  def print_banner(self):
    Color.p("\n               __")
    Color.p("    ..=====.. |{R}=={W}|")   
    Color.p("    ||     || |{B}={W} |     {G}PasswordAlgorithms {D}v%s{W}" % Configuration.version)
    Color.p(" _  ||     || |{R}^{G}*{W}| _   {R}Created: {D}%s{W}" % Configuration.created_on)
    Color.p("|{G}={W}| o=,===,=o |__||{G}={W}|  {B}Author: {D}%s{W}" % Configuration.author)
    Color.p("|_|  _______)~`)  |_|") 
    Color.p("    [=======]  ()\n")     
  def start(self):
    while self.running:
      userIp = input("-[ ")
      if userIp == "quit":
        self.running = False
        sys.exit()

def entry_point():
  try:
    exp = Experiment()
    exp.start()
  except Exception as e:
    Color.p('\n[!] Interuptted, Shutting down...')
    Color.p('[!] %s' % e)
    if e == ConnectionError:
      Color.p('[!] Could be due to SMTP protocol timing out.')