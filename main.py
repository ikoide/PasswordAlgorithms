from environment import Environment

if __name__ == "__main__":
  environment = Environment()
  environment.run(algoType="bruteForce", passType="low", length=4, iterations=4)