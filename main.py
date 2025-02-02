from turtle import Turtle, Screen
from random import randint

turtle_list = []
color_list = ["red", "blue", "green", "cyan", "pink", "purple", "orange", "salmon", "brown", "gray"]
screen = Screen()
screen.setup(width=600, height=500)
goal_x = screen.window_width()/2-50
goal_y = screen.window_height()/2
screen.title(f"Turtle Race")

def create_turtle_list(n_turtles):
    for j in range(n_turtles):
        turtle_list.append(Turtle("turtle"))


def init_positions():
    spacing = screen.window_height() / len(turtle_list)
    start_y = screen.window_height() / 2 - spacing / 2
    for index, turtle in enumerate(turtle_list):
        turtle.penup()
        turtle.color(color_list[index % len(color_list)])
        turtle.goto(x=screen.window_width() * -0.45, y=start_y - index * spacing)


def draw_finish_line():
    assistant = Turtle()
    assistant.penup()
    assistant.goto(x=goal_x, y=goal_y)
    assistant.pendown()
    assistant.right(90)
    assistant.forward(screen.window_height())
    assistant.hideturtle()


def run():
    for turtle in turtle_list:
        turtle.speed("fastest")
        turtle.forward(randint(0, 30))


def game_on():
    for turtle in turtle_list:
        if turtle.xcor() > goal_x:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.title(f"You won! The winner is {winning_color}")
            else:
                screen.title(f"Sorry, you lost! The winner is {winning_color}")
            return False
    return True


def ask_for_turtles():
    user_win_turtles = 0
    while user_win_turtles < 2 or user_win_turtles > 10:
        user_win_turtles = int(screen.textinput(title="How many racers?", prompt="Select between 2 and 10 turtles"))
    create_turtle_list(user_win_turtles)


def make_bet():
    colors = []
    colors_string = ""
    choice = ""

    for new_color in range(len(turtle_list)):
        colors.append(color_list[new_color])

    for new_element in range(len(colors)):
        colors_string += f"\n-{color_list[new_element].upper()}"

    while choice.lower() not in colors:
        choice = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color\n{colors_string}")
    return choice.lower()


ask_for_turtles()
init_positions()
draw_finish_line()
user_bet = make_bet()

while game_on():
    run()
print("Race ended.")

screen.exitonclick()
