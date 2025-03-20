# import random

# def play_rps(player_choice):
#     choices = ["rock", "paper", "scissors"]
#     computer_choice = random.choice(choices)

#     if player_choice == computer_choice:
#         return f"Both chose {player_choice}. It's a tie!"
#     elif (player_choice == "rock" and computer_choice == "scissors") or \
#          (player_choice == "paper" and computer_choice == "rock") or \
#          (player_choice == "scissors" and computer_choice == "paper"):
#         return f"You chose {player_choice}, computer chose {computer_choice}. You win!"
#     else:
#         return f"You chose {player_choice}, computer chose {computer_choice}. You lose!"


# print(play_rps("rock"))
import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(5)

# Heart drawer
def draw_heart():
    turtle.pensize(3)
    turtle.speed(5)
    turtle.color("red")
    
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()
    
    turtle.hideturtle()

# Floating hearts animation
def floating_hearts():
    heart_turtle = turtle.Turtle()
    heart_turtle.speed(0)
    heart_turtle.hideturtle()

    colors = ["red", "pink", "white"]
    
    for _ in range(15):
        heart_turtle.penup()
        heart_turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        heart_turtle.pendown()
        
        heart_turtle.color(random.choice(colors))
        heart_turtle.begin_fill()
        heart_turtle.left(50)
        heart_turtle.forward(15)
        heart_turtle.circle(7, 180)
        heart_turtle.right(90)
        heart_turtle.circle(7, 180)
        heart_turtle.forward(15)
        heart_turtle.end_fill()

        time.sleep(0.2)

# Display romantic message
def show_message():
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.color("white")
    msg.penup()
    msg.goto(-70, -30)
    msg.write("I Love You Kukuu❤️", font=("Arial", 20, "bold"), align="center")

# Run everything with a smooth animation
def main():
    screen.tracer(1)
    draw_heart()
    time.sleep(1)  # Wait before showing animation
    floating_hearts()
    time.sleep(1)
    show_message()
    screen.mainloop()

main()
