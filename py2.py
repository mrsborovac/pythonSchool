import turtle
t = turtle.Turtle()

Guess = int(input("what is 5x5?   "))

if Guess == 5*5:
    t.pencolor("green")
    t.write(str(Guess) + 'is correct! good job', font=("Arial", 30, "normal"), align="center")
    

else:
    t.pencolor("red")
    t.write("tharts wrong!", font=("Arial", 30, "normal"), align="center")

input("press any key..")