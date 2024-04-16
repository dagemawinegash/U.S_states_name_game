import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_names = data.state.tolist()
game_is_on = True
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 states correct", prompt="What is another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missed = [name for name in state_names if name not in correct_guesses]
        missed_states_data = pandas.DataFrame(missed)
        missed_states_data.to_csv("states_to_learn_csv")
        break
    if answer_state in state_names and answer_state not in correct_guesses:
        row = data[data["state"] == answer_state]
        x = int(row["x"])
        y = int(row["y"])
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.color("black")
        answer_turtle.penup()
        answer_turtle.goto(x, y)
        answer_turtle.write(answer_state)
        correct_guesses.append(answer_state)

screen.exitonclick()


