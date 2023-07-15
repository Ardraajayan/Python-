print("Welcome to the quiz world!!!")

start = input("Do you want to start quiz? ")

if start.lower() != "yes":
    quit()

print("Okay! Let's start")

score = 0

answer = input ("Which animal is known as 'ship of the Desert'? ")
if answer.lower() == "camel":
    print("Correct!")
    score+=1
else:
    print("Sorry!!!Incorrect")


answer = input ("Baby frog is known as? ")
if answer.lower() == "tadpole":
    print("Correct!")
    score += 1
else:
    print("Sorry!!!Incorrect")

answer = input ("How many hours are there in a day? ")
if answer == "24":
    print("Correct!")
    score += 1
else:
    print("Sorry!!!Incorrect")

answer = input ("Rainbow consist og how many colours? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Sorry!!!Incorrect")

answer = input ("Name the National animal of India? ")
if answer.lower() == "tiger":
    print("Correct!")
    score += 1
else:
    print("Sorry!!!Incorrect")


print("You got " + str(score) + " questions correct")
print("You got " + str((score/5) * 100) + "%.")