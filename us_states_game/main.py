import turtle
import pandas
from writer import Writer

image = "blank_states_img.gif"
game_data = pandas.read_csv("./50_states.csv")
all_states = game_data["state"].tolist()
correct_answers = []
screen = turtle.Screen()
screen.setup(800, 700)
screen.title("U.S States Game")

answer_writer = Writer()
screen.addshape(image)
turtle.shape(image)
game = True

while game:

    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 State Correct", prompt="What's another state name?")

    if answer_state is None:
        break

    answer_state = answer_state.title()


    if answer_state == "Exit":
        for state in correct_answers:
            if state in all_states:
                all_states.remove(state)
        study_guide = pandas.DataFrame(all_states, columns=["states"])
        study_guide.to_csv("./study_guide.csv")
        screen.title(f"Game Over! Final Score: {len(correct_answers)}/50")
        screen.ontimer(screen.bye, 2000)
        break
    if (game_data["state"] == answer_state).any():
        answer_writer.writer_move(game_data[game_data["state"] == answer_state].x.item(),
                              game_data[game_data["state"] == answer_state].y.item())
        answer_writer.write_answer(answer_state)
        correct_answers.append(answer_state)

    else:
        continue

screen.mainloop()
