#-------------------------------------------------------------------------------
# Name:        Number guessing game 
# Purpose:     Final Project
#
# Author:      cjfalcon-argot
#
# Created:     11/18/2025
# Copyright:   (c) cjfalcon-argot 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

lowest_num = 0
highest_num = 100
guesses = 0
answer = random.randint(lowest_num, highest_num)


def number_guess():
    answer = random.randint(lowest_num, highest_num)
    guesses = 0

    print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")

    while True:
        guess = input("Enter your guess: ")

        # Check if input is a number
        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess)
        guesses += 1

        # Check range
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}.")
            continue

        # Compare guess to answer
        if guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Congratulations! You guessed the number!")
            print(f"The answer was: {answer}")
            print(f"Number of guesses: {guesses}")
            break



while True:# Game menu
    print("\n--- Number Guessing Game Menu ---")
    print("1. Play")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        number_guess()
    elif choice == '2':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")


myfile = open("guessinggame.txt", "w")
myfile.write(f"The answer was: {answer} \n")
myfile.write(f"Number of guesses: {guesses}\n")
myfile.close()

mynewhandle = open("guessinggame.txt", "r")
while True:
    theline = mynewhandle.readline()
    if len(theline) == 0:
        break

    print(theline, end="")

mynewhandle.close()
