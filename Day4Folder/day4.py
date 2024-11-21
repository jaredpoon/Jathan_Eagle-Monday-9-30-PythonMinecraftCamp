# Write all your codes for Day 4 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# print("hello from day4")


# counter = 0
# for counter in range(5):
#     print(counter)

# counter = 0
# while counter < 5:
#     print(counter)
#     counter = counter + 1


# counter = 0
# while counter < 10:
#     print(counter)
#     counter = counter + 1


# counter = 5
# while counter < 33:
#     print(counter)
#     counter += 1

# counter = 50
# while counter > 0:
#     print(counter)
#     counter -= 1



lives = 4
correctAns = "a keyboard"
userAns = input("What has keys, but no lock. Has space, but no room. You can enter, but you cannot leave. ")
while userAns != correctAns:
    lives = lives - 1
    if lives > 0:
        print("Oops, you got it wrong. Try again.")
        userAns = input("What has keys, but no lock. Has space, but no room. You can enter, but you cannot leave. ")
    else:
        print("Boo! You have ran out of lives.")
        break
if lives > 0:
    print("You finally got it right!!!!")