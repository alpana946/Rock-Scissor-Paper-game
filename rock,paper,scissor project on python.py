# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 18:27:22 2021

@author: Alpana
"""

# importing required random module
import random
print("The Rules of Rock paper scissor game: \n"
+ "Rock vs paper == paper wins \n" + "Rock vs scissor == Rock wins \n"
+ "paper vs scissor == scissor wins \n")

print ("Enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")

# input from user
ch = int(input("Now Your turn: "))
while ch> 3 or ch< 1:
   ch = int(input("Enter your valid input: "))
if ch == 1:
 user_choice = 'Rock'
elif ch == 2:
 user_choice = 'paper'
else:
 user_choice = 'scissor'

# print user given choice
print("Your choice is: " + user_choice)
print("\n Now its computer turn to initiate")

# Computer will select randomly any values among 1, 2, 3
comp = random.randint(1, 3)

# variable corresponding to the choice value
if comp == 1:
   comp_choice = 'Rock'
elif comp == 2:
   comp_choice = 'paper'
else:
   comp_choice = 'scissor'
   print("So computer choice is: " + comp_choice)
   print(user_choice + " V/s " + comp_choice)
   
# condition for winning the game
if((ch == 1 and comp == 2) or
   (ch == 2 and comp ==1)):
    print("paper wins => ", end = "")
    final_result = "paper"
elif((ch == 1 and comp == 3) or
   (ch == 3 and comp == 1)):
    print("Rock wins =>", end = "")
    final_result = "Rock"
else:
    print("scissor wins =>", end = "")
    final_result = "scissor"
  
   # Printing either user or computer wins
if final_result == user_choice:
   print("<== You are the winner ==>")
else:
   print("<== Computer wins ==>")