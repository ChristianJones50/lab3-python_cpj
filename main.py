# Author: Christian Jones cpj5199@psu.edu
# Collaborator: Ivy Qi ijq5005@psu.edu
# Collaborator: Zakaria Young zjy5116@psu.edu
# Collaborator: Winston Chen wzc5306@psu.edu
# Collaborator: Remington Navarro rmn5299@psu.edu
# Section: 5
# Breakout Room: 4

def sum_n(n):
  if n >= 1:
    return n + sum_n(n-1)
  else:
    return 0   

def print_n(s, n):
  if n >= 1:
    print(s)
    print_n(s, n-1)
  else:
    return
      
def run():
  intMain = int(input("Enter an int: "))
  print(f"sum is {sum_n(intMain)}.")
  strMain = input("Enter a string: ")
  print_n(strMain, intMain)

if __name__ == "__main__":
  run()