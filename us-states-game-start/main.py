import  turtle
import  pandas

STATES_IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(STATES_IMAGE)
screen.tracer(0)
turtle.shape(STATES_IMAGE)
screen.update()
turtle.penup()

data = pandas.read_csv("50_states.csv")
states_to_guess = data["state"].to_list()

while len(states_to_guess) > 0:
    answer_state = screen.textinput(title=f"Guessed {50 - len(states_to_guess)}/50 ", prompt="What's another state's name ?").title()
    if answer_state in states_to_guess:
        state = data [ data["state"] == answer_state]
        turtle.goto(int(state["x"]), int(state["y"]))
        turtle.write(arg=f"{answer_state}", align="CENTER", font=('Courier', 10, 'normal'))
        states_to_guess.remove(answer_state)

    if answer_state == "Exit":
        pandas.DataFrame(states_to_guess).to_csv("states_to_guess.csv")
        break

