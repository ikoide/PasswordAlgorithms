def dictionaryAttack(password):
  with open("rockyou.txt", "r", encoding="ISO-8859-1") as f:
    data = f.read().splitlines()
    for line in data:
      if password.content == line:
        password.cracked = True