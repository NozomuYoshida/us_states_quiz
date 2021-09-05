import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(width=700, height=500)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)


# answer_state = 'ohio'

data = pandas.read_csv('50_states.csv')
# print(data)
all_states = data.state.to_list()
# print(all_states)
guessed_states = []

# print(answer_state, type(answer_state))
# print('Ohio', type('Ohio'))
# print(answer_state == 'Ohio')

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt='What\'s the another state name?').title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        print('You are right')
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.setpos(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # t.write(state_data.state.item())

    # if any(data['state'] == answer_state):
    #     state = data[data['state'] == answer_state]
    #     print(state)
    #     idx = state.index[0]
    #     print(f'idx: {idx}')
    #     print(state.to_dict())
    #     x = state.to_dict()['x'][idx]
    #     y = state.to_dict()['y'][idx]
    #     print(x, y)

        # turtle.hideturtle()
        # turtle.penup()
        # turtle.setpos(x, y)
        # turtle.write(answer_state, move=False, font=("Arial", 8, "normal"))

states_to_learn = []
for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv('states_to_learn.csv')

screen.exitonclick()