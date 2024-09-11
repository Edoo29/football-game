import random
from time import sleep
import os


def show_goal():
    print("\n --------- \n| 1  2  3 |\n| 4  5  6 |\n")


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


clear_terminal()
home_team = input("Select home team  => ")
away_team = input("Select away team  => ")
number_of_shoots = int(input("How many shoots for each team? "))
home_score: int = 0
away_score: int = 0


def print_result():
    print(f"{home_team} {home_score} - {away_score} {away_team}\n")


while True:
    for i in range(number_of_shoots):
        clear_terminal()
        print_result()
        print(f"{i + 1}/{number_of_shoots}")
        print(f"{home_team} turn!")
        show_goal()
        shoot_direction = int(input("Shoot direction  => "))
        random_cpu_number: int = random.randint(1, 6)
        print(f"({random_cpu_number})")
        if shoot_direction == random_cpu_number:
            print("The goalkeeper saved the goal!")
        else:
            home_score = home_score + 1
            print("GOAAAAL")
        sleep(2)
        clear_terminal()
        print_result()
        print(f"{i + 1}/{number_of_shoots}")
        print(f"{away_team} turn!")
        show_goal()
        shoot_direction = int(input("Shoot direction  => "))
        random_cpu_number: int = random.randint(1, 6)
        print(f"({random_cpu_number})")
        if shoot_direction == random_cpu_number:
            print("The goalkeeper saved the goal!")
        else:
            away_score = away_score + 1
            print("GOAAAAL")
        sleep(2)

    clear_terminal()
    if home_score > away_score:
        print(f"{home_team} won the match!")
        print(f"Final result: {home_team} {home_score} - {away_score} {away_team}")
    elif home_score < away_score:
        print(f"{away_team} won the match!")
        print(f"Final result: {home_team} {home_score} - {away_score} {away_team}")
    else:
        print("Draw!")
        print(f"Final result: {home_team} {home_score} - {away_score} {away_team}")

    sleep(3)
    break
