#imported libraries
import random
import time
import os
from datetime import date

#variables
today = str(date.today())

#sets up the players
print("Axe Throwing: \n")
playerOne = input("Player One:  ") 
os.system('clear')
print("Axe Throwing: \n")
playerTwo = input("Player Two:  ") 
os.system('clear')

#game
print("Throw One: ")
p1t1 = int(input("Player 1: "))
os.system('clear')
print("Throw One: ")
p2t1 = int(input("Player 2: "))
os.system('clear')

print("Throw Two: ")
p1t2 = int(input("Player 1: "))
os.system('clear')
print("Throw Two: ")
p2t2 = int(input("Player 2: "))
os.system('clear')

print("Throw Three: ")
p1t3 = int(input("Player 1: "))
os.system('clear')
print("Throw Three: ")
p2t3 = int(input("Player 2: "))
os.system('clear')

print("Throw Four: ")
p1t4 = int(input("Player 1: "))
os.system('clear')
print("Throw Four: ")
p2t4 = int(input("Player 2: "))
os.system('clear')

print("Throw Five: ")
p1t5 = int(input("Player 1: "))
os.system('clear')
print("Throw Five: ")
p2t5 = int(input("Player 2: "))
os.system('clear')

print("Switch Sides")
time.sleep(3)
os.system('clear')

print("Throw Six: ")
p1t6 = int(input("Player 1: "))
os.system('clear')
print("Throw Six: ")
p2t6 = int(input("Player 2: "))
os.system('clear')

print("Throw Seven: ")
p1t7 = int(input("Player 1: "))
os.system('clear')
print("Throw Seven: ")
p2t7 = int(input("Player 2: "))
os.system('clear')

print("Throw Eight: ")
p1t8 = int(input("Player 1: "))
os.system('clear')
print("Throw Eight: ")
p2t8 = int(input("Player 2: "))
os.system('clear')

print("Throw Nine: ")
p1t9 = int(input("Player 1: "))
os.system('clear')
print("Throw Nine: ")
p2t9 = int(input("Player 2: "))
os.system('clear')

print("Throw Ten: ")
p1t10 = int(input("Player 1: "))
os.system('clear')
print("Throw Ten: ")
p2t10 = int(input("Player 2: "))
os.system('clear')

#some quick addition
p1Sum = (p1t1 + p1t2 + p1t3 + p1t4 + p1t5 + p1t6 + p1t7 + p1t8 + p1t9 + p1t10)
p2Sum = (p2t1 + p2t2 + p2t3 + p2t4 + p2t5 + p2t6 + p2t7 + p2t8 + p2t9 + p2t10)

#open and writes to a file / writes done the score: 
f = open("Score.txt", "a")
f.write("\n")
f.write(today + "\n")
f.write(playerOne + ":  " + str(p1t1) + " " + str(p1t2) + " " + str(p1t3) + " " + str(p1t4) + " " + str(p1t5) + " " + str(p1t6) + " " + str(p1t7) + " " + str(p1t8) + " " + str(p1t9) + " " + str(p1t10) + " = " + str(p1Sum) + "\n")
f.write(playerTwo + ":  " + str(p2t1) + " " + str(p2t2) + " " + str(p2t3) + " " + str(p2t4) + " " + str(p2t5) + " " + str(p2t6) + " " + str(p2t7) + " " + str(p2t8) + " " + str(p2t9) + " " + str(p2t10) + " = " + str(p2Sum))
f.write("\n")
f.close()

#open and read the file after the appending: 
f = open("Score.txt", "r")
print(f.read())