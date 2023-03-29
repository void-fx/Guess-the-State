import turtle
import pandas

screen = turtle.Screen()
screen.title("Nigeria States Game")
image = "Nigerian map void-fx game.gif"
screen.addshape(image)

turtle.shape(image)

guessed_state = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/36 States Correct", prompt="What is another states "
                                                                                            "name").title()
    data = pandas.read_csv("36_states.csv")
    all_states = data.state.to_list()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        if len(guessed_state) < 50:
            game_is_on = True
        else:
            game_is_on = False
