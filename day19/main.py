from turtle import Turtle,Screen
from random import randint
from tkinter import messagebox

# tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
screen.listen()
#
# def move_forward():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_clock_wise():
#     tim.right(10)
#
# def turn_counter_clock_wise():
#     tim.left(10)
#
# def clear_screen():
#     tim.reset()
#
# def scetch():
#     screen.onkey(key="w", fun=move_forward)
#     screen.onkey(key="s", fun=move_backwards)
#     screen.onkey(key="a", fun=turn_counter_clock_wise)
#     screen.onkey(key="d", fun=turn_clock_wise)
#     screen.onkey(key="c", fun=clear_screen)
#
#

def race():
    screen.clear()
    play_some_more = True
    while play_some_more:
        is_race_on = False

        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        all_turtles = []
        for i in range(0, len(colors)):
            turtle = Turtle("turtle")
            turtle.color(colors[i])
            turtle.penup()
            turtle.setx(-230)
            turtle.sety(130 - i * screen.canvheight/len(colors))
            all_turtles.append(turtle)


        user_bet = ""

        while user_bet not in colors:
            user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color {colors}:").lower()

        if user_bet:
            is_race_on = True

        while is_race_on:
            for turtle in all_turtles:
                    turtle.forward(randint(0,10))
                    if turtle.xcor() >= screen.canvwidth/2 - turtle.width():
                        is_race_on = False
                        print(f"Turtle {turtle.pencolor()} is winner!")
                        if user_bet == turtle.pencolor():
                            print("You win.")
                            messagebox.showinfo("Congrats", "You win.")
                        else:
                            print("You loose")
                            messagebox.showinfo("Sorry!", "You loose.")

        should_continue = screen.textinput(title="Want to play moret",
                                    prompt="To continue, press a key. To exit type 'q'").lower()
        if should_continue == 'q':
            play_some_more = False
        else:
            race()



    #screen.exitonclick()

race()