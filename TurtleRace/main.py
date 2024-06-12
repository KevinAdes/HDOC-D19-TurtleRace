from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.colormode(255)

run_race = False
my_screen.setup(width= 500, height= 400)
user_input = my_screen.textinput(title="Place your bet", prompt="Which turtle will win the race?")

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]

race_turtles = []

for _ in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(_)
    new_turtle.penup()
    race_turtles.append(new_turtle)


def move_turtles_to_start():
    for racer_index in range(len(race_turtles)):
        race_turtles[racer_index].goto(x=-250, y=(-100 + 40*racer_index))


if user_input:
    run_race = True


move_turtles_to_start()

while run_race:
    for racer in race_turtles:
        dist_to_move = random.randint(0, 10)
        racer.forward(dist_to_move)

    winning_turtle_indexes = []
    for racer_index in range(len(race_turtles)):
        if race_turtles[racer_index].position()[0] >= 200:
            winning_turtle_indexes.append(racer_index)

    if len(winning_turtle_indexes) > 0:
        my_screen.bye()
        run_race = False
        if len(winning_turtle_indexes) == 1:
            print(f"the winner is {colors[winning_turtle_indexes[0]]}")
            if colors[winning_turtle_indexes[0]] == user_input:
                print("you win!")
            else:
                print("better luck next time")
        else:
            player_won = False
            out_string = "its a tie between "
            for t in range(len(winning_turtle_indexes)):
                out_string += colors[winning_turtle_indexes[t]]
                if user_input == colors[winning_turtle_indexes[t]]:
                    player_won = True
                if t < len(winning_turtle_indexes) - 2:
                    out_string += ", "
                elif t == len(winning_turtle_indexes) - 2:
                    out_string += ", and "
            print(out_string)
            if player_won:
                print("you win!")
            else:
                print("better luck next time")

