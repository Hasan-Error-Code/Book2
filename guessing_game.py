import random

number = random.randint(1, 100)
print("Guess a number between 1 to 100: \n")
num = int(input())

while True:    
    if num == number:
        print("Congratulation you get the number! ", num)
        break
    elif num < number: 
        print("Guess bigger number: ")
    elif num > number:
        print("Guess smaller number: ")
    num = int(input())