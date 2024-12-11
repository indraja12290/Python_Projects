print("welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("1.what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('Oops! Incorrect')

answer = input("2.what does GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print('correct!')
    score += 1
else:
    print('Oops! Incorrect')

answer = input("3.what does RAM stands for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print('Oops! Incorrect')

answer = input("4.what does PSU stands for? ")
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print('Oops! Incorrect')

answer = input("5.what does ROM stands for? ")
if answer.lower() == "read only memory":
    print('correct!')
    score += 1
else:
    print('Oops! Incorrect')

if score == 5:
    print("Congratulations :) You Nailed IT, You got " + str(score) + " questions correct")
else:
    print("Oops! Try one more TIME You got " + str(score) + " questions correct")

print("your score is " + str((score/5)*100 ) + "%.")

