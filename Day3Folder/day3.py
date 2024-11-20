# Write all your codes for Day 3 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# print("hello from day3")


# import time
# name1 = input("What is your name?" + " ")
# for i in name1:
#     time.sleep(1)
#     print("Give me a " + i + "!")
# time.sleep(1)
# print("WHO'S THE BEST?")
# time.sleep(1)
# print("IT'S")
# for i in name1:
#     time.sleep(1)
#     print(i + "!")
# print(name1 + "!!!!")


# num1 = input("What is the first number to add? ")
# num2 = input("What is the second number to add? ")
# ans = int(num1) + int(num2)
# for i in ans():
#     print("The sum of " + num1 + " and " + num2 + " = " + str(ans))


# name2 = input("What is your name? ")
# num_pens = input("How many pens did you buy? ")
# print(name2 + " bought " + num_pens + " pens.")


# num1calc = input("What is the first number? ")
# num2calc = input("What is the second number? ")
# ans1calc = (int(num1calc) + int(num2calc))
# ans2calc = (int(num1calc) - int(num2calc))
# ans3calc = (int(num1calc) * int (num2calc))
# ans4calc = (int(num1calc) / int(num2calc))
# print(num1calc + " + " + num2calc + " = " + str(ans1calc))
# print(num1calc + " - " + num2calc + " = " + str(ans2calc))
# print(num1calc + " x " + num2calc + " = " + str(ans3calc))
# print(num1calc + " ÷ " + num2calc + " = " + str(ans4calc))


# num1calcteacher = int(input("What is the first number? "))
# num2calcteacher = int(input("What is the second number? "))
# print(str(num1calcteacher) + " + " + str(num2calcteacher) + " = " + str(num1calcteacher + num2calcteacher))
# print(str(num1calcteacher) + " - " + str(num2calcteacher) + " = " + str(num1calcteacher - num2calcteacher))
# print(str(num1calcteacher) + " x " + str(num2calcteacher) + " = " + str(num1calcteacher * num2calcteacher))
# print(str(num1calcteacher) + " ÷ " + str(num2calcteacher) + " = " + str(num1calcteacher / num2calcteacher))


# print(10 < 5)
# print(10 > 5)
# print(5 <= 10)
# print(5 <= 5)
# print(5 < 5)
# print(5 == 5)
# print(5 != 5)


# correctPassword = "ABCD"
# userPassword = input("What is the password? ")
# print(correctPassword == userPassword)


# correctPassword = "ABCD"
# userPassword = input("What is the password? ")
# if correctPassword == userPassword:
#     print("Access Granted!")
# if correctPassword != userPassword:
#     print("Access Denied!")


# correctPassword = "ABCD"
# userPassword = input("What is the password? ")
# if correctPassword == userPassword:
#     print("Access Granted!")
# else: 
#     print("Access Denied!")


# person1age = input("What is your age? ")
# person2age = input("What is youur age? ")
# if person1age > person2age:
#     print("Person 1,lease take care of Person 2.")
# elif person1age == person2age:
#     print("Take care of each other and hold hands.")
# else:
#     print("Person 2, please take care of Person 1.")

# import random
# print(random.randint(1, 100))


import random
randomNum = random.randint(1, 5)
userGuess = int(input("Guess a number between 1 and 5: "))
if userGuess == randomNum:
    print("You are correct!!!! You won!!!!")
elif userGuess > randomNum:
    print("You number is too large, try again!")
elif userGuess < randomNum:
    print("Your number is too small, try again!")